# coding:utf-8
from django.shortcuts import render, redirect, HttpResponse, render_to_response
from models import *
import random
import json
import re
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from datetime import datetime


def htmlToPDF(request):
	return