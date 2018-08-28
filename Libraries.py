from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User, Group
from django.db import models
from django.urls import path, re_path, include
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import json