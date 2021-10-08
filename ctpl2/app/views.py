from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
# from django.contrib.auth.models import Group

# Create your views here.
def home(request):
	return render(request,'home.html')


# Change Password

def changepassword(request):
    if request.method=='POST':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
        return redirect('/accounts/login/')
    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'changepass.html',{'form':fm})


    #   Form Code
def addUser(request):
    if request.user.username in ['sayali','ateeq']:
        if request.method=='POST':
            f=UserForm(request.POST)
            
            f.save()
            return redirect("/")
        else:
        	
            f=UserForm
            userC='User Creation Form'
            return render(request,'form.html',{'form':f,'name':userC})
    else:
        return render(request,'error.html')






@login_required
def addDC(request):
    if request.user.username  ['resel','admin']:
 	
        if request.method=='POST':
            f=DCForm(request.POST)
            if f.is_valid():
            	f.save()
            	return redirect('dclist')
        else:
            f=DCForm
            DC_form='DC FORM'
            return render(request,'form.html',{'form':f,'name':DC_form})
    else:
        return HttpResponse('You are not allowed here !')


@login_required
def addProduct(request):
    if request.user.username in ['ateeq','admin','sayali']:
        if request.method=='POST':
            f=ProductForm(request.POST)
            f.save()
            return redirect("/productlist/")
        else:
            f=ProductForm
            BOQ_form='Product FORM'
            return render(request,'form.html',{'form':f,'name':BOQ_form})
    else:
        return render(request,'error.html')


@login_required
def productlist(request):
    if request.user.username in ['admin','rajesh','sunil','ateeq','sayali','lalit','ankit','anil','bhavik','bhimasen','chandraprakash','dewey','dipesh','ishwar','kanhiya','kuldeep','lalit','madhuban','yusuf','manoj','israil'] :
        l=Product.objects.all()
        return render(request,'productlist.html',{'x':l})
    else:
        return HttpResponse('404 Error')


@login_required
def searchProduct(request):
    query=request.GET['query']
    q=Product.objects.filter(Serial_Pak_Number__icontains=query)
    return render(request,'searchProduct.html',{'q1':q})

@login_required
def Coustmersearch(request):
    query=request.GET['query']
    q=Product.objects.filter(Customer_Name__icontains=query)
    return render(request,'searchProduct.html',{'q1':q})


#RMA Code

@login_required
def addRMA(request):
    if request.user.username in ['sayali','admin'] :
        if request.method=='POST':
            f=RMAForm(request.POST)
            f.save()
            return redirect("/")
        else:
            f=RMAForm
            BOQ_form='RMA FORM'
            return render(request,'form.html',{'form':f,'name':BOQ_form})
    else:
        return render(request,'error.html')



@login_required
def RMAlist(request):
    if request.user.username in ['sayali','admin']:
        l=RMA.objects.all().order_by('id')
        paginator=Paginator(l,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        return render(request,'rmalist.html',{'x':page_obj})
    else:
        return render(request,'error.html')

@login_required
def addRMA_Device(request):
    if request.user.username in ['sayali','admin'] :
        if request.method=='POST':
            f=RMA_Device_Form(request.POST)
            f.save()
            return redirect("rmadevicelist")
        else:
            f=RMA_Device_Form
            BOQ_form='RMA FORM'
            return render(request,'form.html',{'form':f,'name':BOQ_form})
    else:
        return render(request,'error.html')

@login_required
def RMAdevicelist(request):
    if request.user.username in ['sayali','admin']:
        l=RMA_Device.objects.all()
        return render(request,'rmadevicelist.html',{'x':l})
    else:
        return render(request,'error.html')

@login_required
def RmaSrsearch(request):
    query=request.GET['Query1']

    q=RMA.objects.filter(SR_Number__icontains=query)
    return render(request,'searchrma.html',{'q1':q})

@login_required
def RmaNumbersearch(request):
    query=request.GET['Query2']
    q=RMA.objects.filter(RMA_Number__icontains=query)
    return render(request,'searchrma.html',{'q1':q})

@login_required
def RmaCustomersearch(request):
    query=request.GET['Query3']
    q=RMA.objects.filter(Customer_name__icontains=query)
    return render(request,'searchrma.html',{'q1':q})

@login_required
def RmaOldsearch(request):
    query=(request.GET['Query4'])
    q=RMA_Device.objects.filter(Old_id=query)
    return render(request,'RmaDeviceSearch.html',{'q1':q})

@login_required
def RmaReplacesearch(request):
    query=request.GET['Query5']
    
    q=RMA_Device.objects.filter(Sr_No__icontains=query)
    return render(request,'RmaDeviceSearch.html',{'q1':q})

# Cop code
# upload cop
@login_required
def upload_Cop(request):
    if request.user.username in ['sneha','admin','sayali']:
        if request.method =='POST':

            form=COPForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/coplist/')
                
        else:
            form=COPForm()
            return render(request,'copupload.html',{'form':form})
    else:
        return render(request,'error.html')

@login_required
def coplist(request):
    if request.user.username in ['sneha','ateeq','rajesh','sunil','admin','sayali'] :
       
        l=COP.objects.all()
       
        
        paginator=Paginator(l,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        return render(request,'coplist.html',{'x':page_obj})
    else:
        return render(request,'error.html')

@login_required
def deletecop(request,id):
    if request.user.username in ['sneha','admin']:
    
        COP.objects.get(id=id).delete()
        return redirect('/coplist/')
    else:
        return redirect('home')



@login_required
def searchCopCompany(request):
    query=request.GET['Query']

    q=COP.objects.filter(Company__Company_Name__icontains=query)
    return render(request,'searchCop.html',{'q1':q})

@login_required
def searchCopProject(request):
    query=request.GET['Query1']
    q=COP.objects.filter(Project__Project_Name__icontains=query)
    return render(request,'searchCop.html',{'q1':q})

@login_required
def searchCopOem(request):
    query=request.GET['Query2']
    q=COP.objects.filter(OEM__OEM_Name__icontains=query)
    return render(request,'searchCop.html',{'q1':q})



#BOQ
@login_required
def Upload_Boq(request):
    if request.user.username in ['niraj','admin','santosh','sayali','ateeq'] :

    

        if request.method =='POST':

            form=BOQForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('boqlist')
                
        else:
            form=BOQForm()
            return render(request,'boqupload.html',{'form':form})

    else:
        return render(request,"error.html")


@login_required
def boqlist(request):
    if request.user.username in ['niraj','admin','rajesh','santosh','sneha','sunil','ateeq','sayali'] :
        return render(request,'minboq.html')
    else:
        return render(request,'error.html')


def fetchboq(request):
    query=request.GET['project']
    
    q=BOQ.objects.filter(Project__Project_Name__icontains=query)
    paginator=Paginator(q,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'boqlist.html',{'x':page_obj}) 


def fetchboq2(request):
    query2=request.GET['company'] 
    q=BOQ.objects.filter(Company__Company_Name__icontains=query2) 
    paginator=Paginator(q,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'boqlist.html',{'x':page_obj})







@login_required
def deleteboq(request,id):
    if request.user.username in ['niraj','santosh'] :
    
        de = BOQ.objects.get(id=id)
        if request.method == 'POST' :
            de.delete()
            return redirect('/boqlist/')
        else:
            return render(request,'confirm_delete.html')
    else:
        return HttpResponse('You arent allowed to delete !!')


@login_required
def deletecompany(request,id):
    if request.user.username in ['sneha','admin'] :
    
        de = Company.objects.get(id=id)
        if request.method == 'POST' :
            de.delete()
            return redirect('/companylist/')
        else:
            return render(request,'company_confirm_delete.html')
    else:
        return HttpResponse('You arent allowed to delete !!')




@login_required
def searchBoqCompany(request):
    query=request.GET['Query']
    q=BOQ.objects.filter(Company__Company_Name__icontains=query)
    return render(request,'searchBoq.html',{'q1':q})

@login_required
def searchBoqProject(request):
    query=request.GET['Query1']
    q=BOQ.objects.filter(Project__Project_Name__icontains=query)
    return render(request,'searchBoq.html',{'q1':q})

@login_required
def searchBoqOem(request):
    query=request.GET['Query2']
    q=BOQ.objects.filter(OEM__OEM_Name__icontains=query)
    return render(request,'searchBoq.html',{'q1':q})



#DC

@login_required
def upload_Dc(request):
    if request.user.username in ['resel','admin','sayali'] :
        if request.method =='POST':

            form=DCForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/dclist/')
                
        else:
            form=DCForm()
            return render(request,'dcupload.html',{'form':form})

    else:
        return render(request,'error.html')

@login_required
def dclist(request):
    if request.user.username in ['niraj','resel','santosh','ateeq','admin','sayali']:
        l=DC.objects.all()
        paginator=Paginator(l,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        return render(request,'dclist.html',{'x':page_obj})
    else:
        return render(request,'error.html')

@login_required 
def deletedc(request,id):
    if request.user.username in ['resel','admin']:
    
        DC.objects.get(id=id).delete()
        return redirect('/dclist/')
    else:
        return render(request,'error.html')



@login_required
def searchDcCompany(request):
    query=request.GET['Query']
    q=DC.objects.filter(Company__Company_Name__icontains=query)
    return render(request,'searchDc.html',{'q1':q})


@login_required 
def searchDcProject(request):
    query=request.GET['Query1']
    q=DC.objects.filter(Project__Project_Name__icontains=query)
    return render(request,'searchDc.html',{'q1':q})

@login_required
def searchDcOem(request):
    query=request.GET['Query2']
    q=DC.objects.filter(OEM__OEM_Name__icontains=query)
    return render(request,'searchDc.html',{'q1':q})


#IR

@login_required
def upload_Ir(request):
    if request.user.username in ['lalit','admin','ateeq','sayali']:
        if request.method =='POST':

            f=IRForm(request.POST,request.FILES)
            if f.is_valid():
                f.save()
                return redirect('irlist')
                
        else:
           
            form=IRForm()
            return render(request,'irupload.html',{'form':form})
    else:
        return render(request,'error.html')


@login_required
def irlist(request):
    if request.user.username in ['lalit','admin','ateeq','ramanshu','sayali']:
        l=IR.objects.all()
        paginator=Paginator(l,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        return render(request,'irlist.html',{'x':page_obj})
    else:
        return render(request,'error.html')

@login_required
def deleteir(request,id):
    if request.user.username in ['lalit']:
    
        IR.objects.get(id=id).delete()
        return redirect('/irlist/')
    else:
        return HttpResponse("You arent allowed here !!")



@login_required
def deletermadevice(request,id):
    if request.user.username in ['sayali','admin','ateeq']:
    
        RMA_Device.objects.get(id=id).delete()
        return redirect('/rmadevicelist/')
    else:
        return HttpResponse("You arent allowed here !!")






@login_required
def searchIrCompany(request):
    query=request.GET['Query']
    q=IR.objects.filter(Company__Company_Name__icontains=query)
    return render(request,'searchIr.html',{'q1':q})



@login_required
def searchIrProject(request):
    query=request.GET['Query1']
    q=IR.objects.filter(Project__Project_Name__icontains=query)
    return render(request,'searchIr.html',{'q1':q})



@login_required
def searchIrOem(request):
    query=request.GET['Query2']
    q=IR.objects.filter(OEM__OEM_Name__icontains=query)
    return render(request,'searchIr.html',{'q1':q})

#All Update Class Base views
class IRupdateview(LoginRequiredMixin,UpdateView):
    model=IR
    template_name='updateir.html'
    fields='__all__'


class Productupdateview(LoginRequiredMixin,UpdateView):
    model=Product
    template_name='updateproduct.html'
    fields='__all__'


class DCupdateview(LoginRequiredMixin,UpdateView):
    model=DC
    template_name='updatedc.html'
    fields='__all__'

class COPupdateview(LoginRequiredMixin,UpdateView):
    model=COP
    template_name='updatecop.html'
    fields='__all__'



# def update_boq(request,id):
#     if request.method=='POST':
#         pi=BOQ.objects.get(id=id)
#         fm=BOQ_form(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#         else:
#             pi=BOQ.objects.get(id=id)
#             fm=BOQ_form(instance=pi)
#         return render(request,'update-boq.html',{'form':fm})


class BOQupdateview(LoginRequiredMixin,UpdateView):
    model=BOQ
    template_name='updateboq.html'
    fields='__all__'


class RMAupdateview(LoginRequiredMixin,UpdateView):
    model=RMA
    template_name='updaterma.html'
    fields='__all__'


class RMAdeviceupdateview(LoginRequiredMixin,UpdateView):
    

    model=RMA_Device
    template_name='updatermadevice.html'
    fields='__all__'

@login_required
def addCompany(request):
    if request.user.username in ['sneha','admin']:
    
        if request.method=='POST':
            f=CompanyForm(request.POST)
            f.save()
            return redirect("Companylist")
        else:
            f=CompanyForm
            BOQ_form='Company FORM'
            return render(request,'form.html',{'form':f,'name':BOQ_form})
    else:
        return HttpResponse("You Arent Allowed Here !!")

@login_required
def companylist(request):
    if request.user.username in ['sneha','admin']:
        li=Company.objects.all()
        paginator=Paginator(li,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        company_data={'x':page_obj}
        return render(request,'companylist.html',context=company_data)
    return HttpResponse('You Arent Allowed Here !!')


@login_required
def addOEM(request):
    if request.user.username in ['sneha','admin']:
    
        if request.method=='POST':
            f=OEMForm(request.POST)
            f.save()
            return redirect("OEMlist")
        else:
            f=OEMForm
            BOQ_form='OEM FORM'
            return render(request,'form.html',{'form':f,'name':BOQ_form})
    else:
        return HttpResponse("You Arent Allowed Here !!")

@login_required
def OEMlist(request):
    if request.user.username in ['sneha','admin']:
        li=OEM.objects.all()
        paginator=Paginator(li,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        company_data={'x':page_obj}
        return render(request,'OEMlist.html',context=company_data)
    return HttpResponse('You Arent Allowed Here !!')

@login_required
def addProject(request):
    if request.user.username in ['sneha','admin']:
    
        if request.method=='POST':
            f=ProjectForm(request.POST)
            f.save()
            return redirect("projectlist")
        else:
            f=ProjectForm
            BOQ_form='Project FORM'
            return render(request,'form.html',{'form':f,'name':BOQ_form})

    else:
        return HttpResponse("You Arent Allowed Here !!")


@login_required
def Projectlist(request):
    if request.user.username in ['sneha','admin'] :
        li=Project.objects.all()
        paginator=Paginator(li,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        company_data={'x':page_obj}
        return render(request,'projectlist.html',context=company_data)
    return HttpResponse('You Arent Allowed Here !!')



@login_required
def deleteproject(request,id):
    if request.user.username in ['sneha','admin'] :
    
        de = Project.objects.get(id=id)
        if request.method == 'POST' :
            de.delete()
            return redirect('/projectlist/')
        else:
            return render(request,'project_confirm_delete.html')
    else:
        return HttpResponse('You arent allowed to delete !!')



@login_required
def deleteOEM(request,id):
    if request.user.username in ['sneha','admin'] :
    
        de = OEM.objects.get(id=id)
        if request.method == 'POST' :
            de.delete()
            return redirect('/OEMlist/')
        else:
            return render(request,'OEM_confirm_delete.html')
    else:
        return HttpResponse('You arent allowed to delete !!')


@login_required
def deleteproduct(request,id):
    if request.user.username in ['sneha','admin'] :
    
        de = Product.objects.get(id=id)
        if request.method == 'POST' :
            de.delete()
            return redirect('/productlist/')
        else:
            return render(request,'product_confirm_delete.html')
    else:
        return HttpResponse('You arent allowed to delete !!')


class OEMupdateview(LoginRequiredMixin,UpdateView):
    model=OEM
    template_name='updateOEM.html'
    fields='__all__'
    success_url='/OEMlist/'

class Projectupdateview(LoginRequiredMixin,UpdateView):
    model=Project
    template_name='updateproject.html'
    fields='__all__'
    success_url='/projectlist/'


class Companyupdateview(LoginRequiredMixin,UpdateView):
    model=Company
    template_name='updateCompany.html'
    fields='__all__'
    success_url='/companylist/'


@login_required
def customcop(request):
    if request.user.username in ['admin','ateeq','sneha']:
        query=request.GET
        l=[]
        l=COP.objects.all()
        company=query.get('Company')
        oem=query.get('OEM')
        project=query.get('project')
        
        if company!='':
            l=l.filter(Company__Company_Name=company)
        if oem!='':
            l=l.filter(OEM__OEM_Name=oem)
        if project!='':
            l=l.filter(Project__Project_Name=project)

        



        c=Company.objects.all()
        o=OEM.objects.all()
        p=Project.objects.all()
        return render(request,'customcop.html',{'l':l,'c':c,'o':o,'p':p})
    return render(request,'error.html')