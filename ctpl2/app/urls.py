from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home,name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('adduser/',addUser,name='new_user'),
    path('changepassword/',changepassword,name='changepass'),
    #DC
    path('upload_Dc/',upload_Dc),
    path('dclist/',dclist,name='dclist'),
    path('searchDcCompany/',searchDcCompany),
    path('searchDcProject/',searchDcProject),
    path('searchDcOem/',searchDcOem),
    path('updateDC/<int:pk>/',DCupdateview.as_view()),

    #COP
    path('upload_Cop/',upload_Cop),
    path('coplist/',coplist,name='coplist'),
    path('searchCopCompany/',searchCopCompany),
    path('searchCopProject/',searchCopProject),
    path('searchCopOem/',searchCopOem),
    path('updateCOP/<int:pk>/',COPupdateview.as_view()),
    #BOQ
    path('upload_Boq/',Upload_Boq),
    path('boqlist/',boqlist,name='boqlist'),
    path('boq-delete/<int:id>/',deleteboq),
    path('searchBoqCompany/',searchBoqCompany),
    path('searchBoqProject/',searchBoqProject),
    path('searchBoqOem/',searchBoqOem),
    path('updateBOQ/<int:pk>/',BOQupdateview.as_view()),
    path('fetchboq/',fetchboq),
    path('fetchboq2/',fetchboq2),
    # path('update-boq/<int:id>/',update_boq),
    #IR
    path('upload_Ir/',upload_Ir),
    path('irlist/',irlist,name='irlist'),
    path('searchIrCompany/',searchIrCompany),
    path('searchIrProject/',searchIrProject),
    path('searchIrOem/',searchIrOem),
    path('updateIR/<int:pk>/',IRupdateview.as_view()),
    path('delete-ir/<int:id>/',deleteir),

    # product deleteproduct
    path('add_product/',addProduct),
    path('productlist/',productlist,name='productlist'),
    path('productsearch/',searchProduct),
    path('Coustmersearch/',Coustmersearch),
    path('updateProduct/<int:pk>/',Productupdateview.as_view()),


    # RMA
    path('addRMA/',addRMA),
    path('rmalist/',RMAlist,name='rmalist'),
    path('RmaSrsearch/',RmaSrsearch),
    path('RmaNumbersearch/',RmaNumbersearch),
    path('RmaCustomersearch/',RmaCustomersearch),
    path('RmaOldsearch/',RmaOldsearch),
    path('RmaReplacesearch/',RmaReplacesearch),
    path('updateRMA/<int:pk>/',RMAupdateview.as_view()),
    path('rmadevice/',addRMA_Device),
    path('rmadevicelist/',RMAdevicelist,name='rmadevicelist'),
    path('updatermadevice/<int:pk>/',RMAdeviceupdateview.as_view()),
    path('deletermadevice/<int:id>/',deletermadevice),
    # add other things  deletermadevice

    path('addCompany/',addCompany),
    path('addOEM/',addOEM),
    path('addProject/',addProject),
    path('companylist/',companylist,name='companylist'),
    path('company-delete/<int:id>/',deletecompany),
    path('OEMlist/',OEMlist,name='OEMlist'),
    path('projectlist/',Projectlist,name='projectlist'),
    path('project-delete/<int:id>/',deleteproject),
    path('OEM-delete/<int:id>/',deleteOEM),
    path('deleteproduct/<int:id>/',deleteproduct),
    path('deletecop/<int:id>/',deletecop),
    path('deletedc/<int:id>/',deletedc),

    path('updateOEM/<int:pk>/',OEMupdateview.as_view()),
    path('updateProject/<int:pk>/',Projectupdateview.as_view()),

    path('Companyupdateview/<int:pk>/',Companyupdateview.as_view()),
    path('customcop/',customcop,name='customcop/?Company=&OEM=&project='),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

