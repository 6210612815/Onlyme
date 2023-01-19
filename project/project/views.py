from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from database.models import Student, StudentForm
import requests, json, sys

def index(request):
    return render(request, "index.html")

def homepage(request):
    return render(request, "homepage.html")

def category(request):
    return render(request, "category.html")

def service(request):
    return render(request, "service.html")

def mycart(request):
    return render(request, "mycart.html")

def editprofile(request):
    return render(request, "editprofile.html")

def profile(request):
    try :
        access_token = request.POST.get('access_token')
        params = {
            'access_token': access_token,
        }
        check_verify_response = requests.get('https://api.line.me/oauth2/v2.1/verify', params=params)

        if check_verify_response.status_code == status.HTTP_200_OK:
            headers = {
                'Authorization':f'Bearer {access_token}',
            }
            response = requests.get('https://api.line.me/v2/profile', headers=headers)
            userId = json.loads(response.text)["userId"]

            if(Student.objects.filter(userId=userId).exists()):
                student = Student.objects.get(userId=userId)
                data = {
                    "fname" : student.fname,
                    "lname" : student.lname,
                    "tel" : student.tel,
                    "sid" : student.sid,
                    "email" : student.email,

                }
                return HttpResponse(json.dumps(data), content_type='application/json')  
    except Exception as e:
        print("{0} : {1}".format(sys.exc_info()[-1].tb_lineno,str(e)))
        return HttpResponse(json.dumps({'message': 'Get some errors2'},default=str), content_type="application/json")
    return render(request, "profile.html")
    
def lineapi(request):
    try :
        access_token = request.POST.get('access_token')
        params = {
            'access_token': access_token,
        }
        check_verify_response = requests.get('https://api.line.me/oauth2/v2.1/verify', params=params)

        if check_verify_response.status_code == status.HTTP_200_OK:
            headers = {
                'Authorization':f'Bearer {access_token}',
            }
            response = requests.get('https://api.line.me/v2/profile', headers=headers)
            userId = json.loads(response.text)["userId"]

            data = {
                "in_db": Student.objects.filter(userId=userId).exists()
            }

            return HttpResponse(json.dumps(data), content_type='application/json')  

    except Exception as e:
        print("{0} : {1}".format(sys.exc_info()[-1].tb_lineno,str(e)))
        return HttpResponse(json.dumps({'message': 'Get some errors'},default=str), content_type="application/json")


def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print('post')
        if form.is_valid():
            print("saved")
            form.save()
            return render(request, 'homepage.html')
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})
