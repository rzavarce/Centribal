"""Users views."""

# Django REST Framework
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers

from rest_framework import status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

# Serializers
from users.serializers import *

# Models
from users.models import UserProfile, TYPE_USER
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.core.mail import EmailMessage
from django.core.mail import send_mail

from django.utils.encoding import force_bytes, force_str
from core.settings import FRONT_URL


class UserApiViewset(generics.ListCreateAPIView):
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserModelSerializer


class LoginViewset(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        if user.status:
            data = {
                'user': UserModelSerializer(user).data,
                'token': token
            }
            return Response(data, status=status.HTTP_200_OK)

        error_msg = {
            "non_field_errors": ["Email no confirmed, pleases check your "
                                 "mail box."]
        }

        return Response(error_msg, status=status.HTTP_401_UNAUTHORIZED)


class LogoutViewset(APIView):

    def post(self, request):
        """User sign out."""

        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        logout(request)

        return Response({"success": _("Successfully logged out.")},
                        status=status.HTTP_200_OK)


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


def ConfirmAccountView(request, uidb64, token):
    """Email User confirm."""

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserProfile.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None

    account_activation_token = TokenGenerator()
    if user is not None and account_activation_token.check_token(user,
                                                                 token):
        user.is_active = True
        user.status = True
        user.save()
        login(request, user)

        message = render_to_string('emails/user_confirm_message.html', {
            'user': user.id,
            'domain': FRONT_URL,
        })
        return HttpResponse(message)
    else:
        return HttpResponse('Activation link is invalid!')


class PasswordResetSendEmailView(APIView):
    """Email User confirm."""
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')

        user = UserProfile.objects.get(email=email)

        if user is not None:

            account_activation_token = TokenGenerator()

            mail_subject = 'Account Password Reset '
            msg_txt = render_to_string('emails/user_reset_password.txt', {
                'domain': FRONT_URL,
                'uid': user.pk,
                'token': account_activation_token.make_token(user),
            })

            msg_html = render_to_string('emails/user_reset_password.html', {
                'domain': FRONT_URL,
                'uid': user.pk,
                'token': account_activation_token.make_token(user),
            })

            to_email = user.email
            send_mail(
                mail_subject,
                msg_txt,
                'no-replay@centribal.com',
                [to_email],
                html_message=msg_html,
            )

            return HttpResponse('Email Password Reset Sended!')


class PasswordResetConfirmView(APIView):
    """Email User confirm."""
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user = UserProfile.objects.get(pk=request.data.get("user"))
        user.set_password(request.data.get("password"))
        user.save()
        response = {
            'status': 'OK',
            'code': status.HTTP_200_OK,
            'message': 'Password updated successfully',
            'data': []
        }

        return Response(response)


class SettingPasswordView(APIView):
    """
    An endpoint for changing password.
    """

    def post(self, request,):

        user = UserProfile.objects.get(pk=request.data.get("user"))
        user.set_password(request.data.get("password"))
        user.save()
        response = {
            'status': 'OK',
            'code': status.HTTP_200_OK,
            'message': 'Password updated successfully',
            'data': []
        }

        return Response(response)


class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """

    def post(self, request,):

        user = UserProfile.objects.get(pk=request.data.get("user"))
        if user.check_password(request.data.get("current_password")):
            user.set_password(request.data.get("new_password"))
            user.save()
            response = {
                'status': 'OK',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status': 'error',
                'code': status.HTTP_401_UNAUTHORIZED,
                'message': 'Current password is not valid.',
                'data': []
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class UsersAddFormData(APIView):

    def get(self, request,):
        """ GET Request to List Form Data"""

        form_data = dict()

        form_data["user_types_list"] = [
            {'value': k, 'label': v} for k, v in TYPE_USER]

        history_query = UserProfile.history.all()[:10]
        form_data["users_history"] = \
            UserHistorySerializer(history_query, many=True).data

        return Response(form_data, status=status.HTTP_200_OK)

    def post(self, request):
        """User sign up."""

        request.data['status'] = False
        request.data['phone_number'] = request.data[
            'phone_number'].replace(" ", "")

        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        account_activation_token = TokenGenerator()

        current_site = get_current_site(request)
        mail_subject = 'Activate your blog account.'
        msg_txt = render_to_string('emails/user_confirm_account.txt', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        msg_html = render_to_string('emails/user_confirm_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        to_email = user.email
        send_mail(
            mail_subject,
            msg_txt,
            'no-replay@centribal.com',
            [to_email],
            html_message=msg_html,
        )

        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)


class UsersEditFormData(APIView):

    def get(self, request, pk):
        """ GET Request to List Form Data"""

        form_data = dict()

        user = UserProfile.objects.filter(id=pk)

        form_data["user_data"] = UserModelSerializer(user, many=True).data

        form_data["user_types_list"] = [
            {'value': k, 'label': v} for k, v in TYPE_USER]

        history_query = UserProfile.history.all()[:10]
        form_data["users_history"] = \
            UserHistorySerializer(history_query, many=True).data

        return Response(form_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """User sign up."""

        qs = UserProfile.objects.get(id=pk)
        serializer = UserModelSerializer(qs, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsersDeleteFormData(APIView):

    def delete(self, request, pk):
        """User delete."""

        qs = UserProfile.objects.get(id=pk)
        qs.delete()

        response = {
            'status': 'OK',
            'code': status.HTTP_200_OK,
            'message': 'User deleted successfully',
            'data': []
        }

        return Response(response, status=status.HTTP_204_NO_CONTENT)
