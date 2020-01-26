from django.shortcuts import render
from .models import Data;
from django.shortcuts import redirect
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from pyexcel_xlsx import save_data
from django.utils.datastructures import MultiValueDictKeyError
import json

# Create your views here.

def get_input(request):

    #return render(request,'index.html');
    return render(request, 'upload.html')



def get_index(request):
    return render(request, 'index.html');

def get_input_post(request):
    #print("I am called")
    try:
        excel_file = request.FILES['files']
        print("hello world");
        if (str(excel_file).split('.')[-1] == "xls"):
            data = xls_get(excel_file)
            print(data);
            print("xls file called");
        elif (str(excel_file).split('.')[-1] == "xlsx"):
            data = xlsx_get(excel_file)
            print("xlsx file called");
        else:
            return render(request, 'index.html')

        json_data = json.dumps(data)
        #print(json_data)

        j=1;
        for i in range(5):
            data['Sheet1'][i+1][j] = str(int(data['Sheet1'][i+1][j])+int(data['Sheet1'][i+1][j]));
            print(data['Sheet1'][i+1][j])

        save_data("my_output.xlsx",data);

        return render(request, 'success.html')


    except MultiValueDictKeyError:
        return render(request, 'index.html')

