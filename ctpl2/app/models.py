from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.

class Company(models.Model):
	Company_Name=models.CharField(max_length=100)
	Location=models.CharField(max_length=100)
	Contact_Person1=models.CharField(max_length=100)
	Contact_Person2=models.CharField(max_length=100,blank=True,null=True)
	Contact1=models.IntegerField(blank=True,null=True)
	Contact2=models.IntegerField(blank=True,null=True)
	Contact3=models.IntegerField(blank=True,null=True)


	def __str__(self):
		return self.Company_Name


class Project(models.Model):
	Project_Name=models.CharField(max_length=100)
	Location=models.CharField(max_length=100)
	Start_Date=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.Project_Name

  


class OEM(models.Model):
    OEM_Name=models.CharField(max_length=100)

    def __str__(self):
        return self.OEM_Name





    


class BOQ(models.Model):
	BOQ_Name=models.CharField(max_length=100)
	Company=models.ForeignKey(Company,on_delete=models.CASCADE)
	Project=models.ForeignKey(Project,on_delete=models.CASCADE)
	OEM=models.ForeignKey(OEM,on_delete=models.CASCADE)
	Date_Created=models.DateField(auto_now_add=True)
	Date_Modified=models.DateField(auto_now=True)
	Remark=models.TextField()
	Upload_BOQ=models.FileField(upload_to='BOQ/files/')


	def get_absolute_url(self):
		return reverse('boqlist')

	def __str__(self):
		return self.BOQ_Name


#class CreateCompany(models.Model):
 #   company_name=models.CharField(max_length=50)
  #  Description=models.TextField()
   # Address=models.TextField()


    #def __str__(self):
     #   return self.company_name
  




class Product(models.Model):
    amc_list=(
        ('contract','Contract'),
        ('CTPL','CTPL'),
        ('both','BOTH')
            ) 
    #Customer_Name=models.ForeignKey(CreateCompany,on_delete=models.CASCADE,default='Godrej')
    Customer_Name=models.CharField(max_length=50)
    Contact_Number=models.IntegerField()
    Customer_Location=models.TextField()
    Product_Part_Number=models.CharField(max_length=50)
    Serial_Pak_Number=models.CharField(max_length=50)
    Refrence_Service_Part_Number=models.CharField(max_length=50)
    PO_Number=models.CharField(max_length=50)
    SO_Number=models.CharField(max_length=50)
    COP_Number=models.CharField(max_length=50)
    Contract_Number=models.CharField(max_length=50)
    Quote_Number=models.CharField(max_length=50)
    Start_Date=models.CharField(max_length=50)
    End_Date=models.CharField(max_length=50)
    Remark=models.TextField()
    AMC=models.CharField(choices=amc_list,default=None,max_length=50)
    License_PartID=models.CharField(max_length=50)
    License_OrderNo=models.CharField(max_length=50)
    License_SO=models.CharField(max_length=50)
    License_PAK=models.CharField(max_length=50)
    License_Description=models.TextField()
    License_Quantity=models.IntegerField()
    License_Start_Date=models.CharField(max_length=50)
    License_End_Date=models.CharField(max_length=50)
    License_Remark=models.TextField()

    def get_absolute_url(self):
        return reverse('productlist')


class RMA(models.Model):

    Sr_No=models.IntegerField()
    Call_Time_CMD=models.CharField(max_length=20)
    Call_Log_Date=models.CharField(max_length=20)
    RMA_Raised_Time=models.CharField(max_length=20)
    SR_Number=models.IntegerField()
    RMA_Number=models.IntegerField()
    Customer_name=models.CharField(max_length=30)
    Location_name=models.CharField(max_length=30)
    Contact_Name=models.CharField(max_length=30)
    Contact_Details=models.IntegerField()
    Faulty_Part_Type=models.CharField(max_length=30)
    Faulty_Part_make_and_Model=models.CharField(max_length=30)
    Faulty_Router_Serial =models.CharField(max_length=30)
    RMA_Make_and_Modem=models.CharField(max_length=30)
    RMA_Serial_Number=models.CharField(max_length=30)
    Fault_Logged_discription=models.CharField(max_length=30)
    Troubleshootings=models.CharField(max_length=30)
    RMA_Approved_Date=models.CharField(max_length=30)
    RMA_Received_CTPL=models.CharField(max_length=30)
    RMA_Delivered_Date=models.CharField(max_length=30)
    Faulty_Part_replacement_status_Pickup_Done_or_Not=models.CharField(max_length=30)
    Faulty_Part_pick_up_Date=models.CharField(max_length=30)
    Faulty_Part_pick_up_Time=models.CharField(max_length=30)
    Remark=models.CharField(max_length=30) 

    def get_absolute_url(self):
        return reverse('rmalist')


    def __str__(self):
    	return str(self.id)



class RMA_Device(models.Model):
    Old_id=models.ForeignKey(RMA,on_delete=models.CASCADE)
    Sr_No=models.IntegerField()
    Remark=models.CharField(max_length=30)

    def get_absolute_url(self):
    	return reverse('rmadevicelist')
    



class IR(models.Model):
	IR_Name=models.CharField(max_length=100)
    
	Company=models.ForeignKey(Company,on_delete=models.CASCADE)
	Project=models.ForeignKey(Project,on_delete=models.CASCADE)
	OEM=models.ForeignKey(OEM,on_delete=models.CASCADE)
	Date_Created=models.DateField(auto_now_add=True)
	Date_Modified=models.DateField(auto_now=True)
	Remark=models.TextField()
	Upload_IR=models.FileField(upload_to='IR/files/')


	def get_absolute_url(self):
		return reverse('irlist')


	def __str__(self):
		return self.IR_Name


	






class DC(models.Model):
	DC_Name=models.CharField(max_length=100)
	Company=models.ForeignKey(Company,on_delete=models.CASCADE)
	Project=models.ForeignKey(Project,on_delete=models.CASCADE)
	OEM=models.ForeignKey(OEM,on_delete=models.CASCADE)
	Date_Created=models.DateField(auto_now_add=True)
	Date_Modified=models.DateField(auto_now=True)
	Remark=models.TextField()
	Upload_DC=models.FileField(upload_to='DC/files/')
	

	def get_absolute_url(self):
		return reverse('dclist')

	def __str__(self):
		return self.DC_Name






class COP(models.Model):
	COP_Name=models.CharField(max_length=100)
	Company=models.ForeignKey(Company,on_delete=models.CASCADE)
	Project=models.ForeignKey(Project,on_delete=models.CASCADE)
	OEM=models.ForeignKey(OEM,on_delete=models.CASCADE)
	Date_Created=models.DateField(auto_now_add=True)
	Date_Modified=models.DateField(auto_now=True)
	Remark=models.TextField()
	Upload_COP=models.FileField(upload_to='COP/files/')


	def get_absolute_url(self):
		return reverse('coplist')

 #customcop/?Company=&OEM=&project=   
       

	def __str__(self):
		return self.COP_Name



