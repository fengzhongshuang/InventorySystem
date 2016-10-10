from django import forms


class borrow_material_form(forms.Form):
    goods_id = forms.IntegerField()
    goods_part_num = forms.CharField()
    goods_spec = forms.CharField()
    goods_revision = forms.CharField()
    goods_location = forms.CharField()
    goods_unit = forms.CharField()
    goods_onhand_qty = forms.IntegerField()
    goods_borrow_qty = forms.IntegerField()
    goods_borrow_date = forms.DateField()
