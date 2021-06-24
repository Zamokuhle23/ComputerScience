from django.shortcuts import render, redirect
from django.views import View
from store.models import Customer
from users.models import User, Seller, DeliverMan


class Signup(View):
    def get(self, request):
        return render(request, 'registration/signup.html')

    def post(self, request):
        userData = request.POST
        print(userData["role"])
        # validate
        error = self.validateData(userData)
        if error:

            return render(request, 'registration/signup.html', {"error": error, "userData": userData})
        else:
            if User.emailExits(userData['email']):
                error["emailExits_error"] = "Email Already Exits"
                return render(request, 'registration/signup.html', {"error": error, "userData": userData})
            else:

                user = User.objects.create_user(
                    username=userData["username"],
                    email=userData["email"],
                    password=userData["password"]
                )
                user.save()
                if userData["role"] == 'Customer':
                    customer = Customer(
                        customer=user,
                        email=userData["email"]
                    )
                    user.is_customer = True
                    user.save()
                    customer.save()
                elif userData["role"] == 'Seller':

                    seller = Seller(
                        seller=user,
                        email=userData["email"]
                    )
                    user.is_seller = True
                    user.save()
                    seller.save()
                elif userData["role"] == 'Seller':
                    deliver = DeliverMan(
                        deliver=user,
                        email=userData["email"]
                    )
                    user.is_deliverman = True
                    user.save()
                    deliver.save()

                return redirect('home')
#sondo mani
    # Validate form method
    def validateData(self, userData):
        error = {}
        if not userData['username'] or not userData['email'] or not userData['role'] or not userData['password'] or not \
                userData['confirm_password']:
            error["field_error"] = "All field must be required"
        elif len(userData['password']) < 8 and len(userData['confirm_password']) < 8:
            error['minPass_error'] = "Password must be 8 char"
        elif len(userData['name']) > 25 or len(userData['username']) < 3:
            error["name_error"] = "Name must be 3-25 charecter"
        elif userData['role'] == 'None':
            error["role_error"] = "select type of registration"
        elif userData['password'] != userData['confirm_password']:
            error["notMatch_error"] = "Password doesn't match"

        return error
