from  django import  forms
from .models import Overtime_work,Time_off

class Work_Time_Form(forms.ModelForm):
    class Meta:
        model = Overtime_work
        fields = ['body','start_time','end_time','work_time','oa_user']

class Off_Time_Form(forms.ModelForm):
    class Meta:
        model = Time_off
        fields = ['body','start_time','end_time','off_time','oa_user']
