from django.shortcuts import render
from django.views import View
from sales.models import Sale
from products.models import Product, Category


MAX_DESKS = 200


class CreateSalePDV(View):
    def get(self, *args, **kwargs):
        desks = self.get_open_desks()
        products = Product.objects.all()
        categories = Category.objects.all()

        return render(
            self.request,
            'pdv.html',
            {
                'desks': desks,
                'products': products,
                'categories': categories
            }
        )

    def get_open_desks(self):
        open_sales = Sale.objects.filter(is_open=True)
        open_desks = {
            sale.desk_number: sale
            for sale in open_sales
        }
        desks = []

        for number in range(1, MAX_DESKS + 1):
            sale = open_desks.get(number)

            desks.append({
                'number': number,
                'is_open': bool(sale),
                'sale_id': sale.id if sale else None,
            })
        return desks
