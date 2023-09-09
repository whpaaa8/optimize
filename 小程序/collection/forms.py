from django import forms
from .models import CollectionInfo

# 收集表表单
class CollectionForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        exclude = ['submit_date']
        model = CollectionInfo

    images = forms.ImageField(label='选择多个文件', help_text='提示：注意只能上传图片',
                              widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    testResult = forms.ImageField(label='选择多个文件', help_text='提示：注意只能上传图片',
                                  widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    position = forms.ImageField(label='选择多个文件', help_text='提示：注意只能上传图片',
                                widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    desc = forms.ImageField(label='选择多个文件', help_text='提示：注意只能上传图片',
                            widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    testReport = forms.FileField(label='选择多个文件', help_text='提示：上传测试报告/需求报告',
                                 widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    def save(self, paths, commit=True):
        collection = super().save(commit=False)
        # print(paths)
        collection.images_path = paths['相关图片']
        collection.testResult_path = paths['掌上优测试截图']
        collection.location = paths['问题定位图']
        collection.testReport_path = paths['测试报告或需求报告']
        collection.desc_path = paths['已解决说明']
        # print(collection)
        if commit:
            collection.save()
            return collection
        else:
            return


class CollectionTestFrom(forms.ModelForm):
    class Meta:
        model = CollectionInfo
        fields = '__all__'
        exclude = ['submit_date']
