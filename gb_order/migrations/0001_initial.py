# Generated by Django 2.1.2 on 2019-03-28 09:03

from django.db import migrations, models
import django.db.models.deletion
import gb_order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gb_merchant', '0001_initial'),
        ('gb_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AOrders',
            fields=[
                ('orderid', models.CharField(help_text='md5加密', max_length=32, primary_key=True, serialize=False, verbose_name='订单号')),
                ('oPhone', models.DecimalField(decimal_places=0, help_text='11位', max_digits=11, verbose_name='联系电话')),
                ('oPrice', models.DecimalField(decimal_places=2, help_text='0.00-99999.99元', max_digits=7, verbose_name='价格')),
                ('oTime', models.DateTimeField(verbose_name='预约时间')),
                ('oDesc', models.TextField(help_text='最大50位', max_length=50, verbose_name='订单备注')),
                ('qrCode', models.ImageField(upload_to=gb_order.models.Orders.order_qrcode_path, verbose_name='二维码')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='订单创建时间')),
                ('oStatus', models.CharField(choices=[('yxd', '用户已下单'), ('yzf', '用户已支付'), ('yjd', '商家已接单'), ('yjs', '订单已结束')], help_text='yxd-用户已下单 yzf-用户已支付 yjd-商家已接单 yjs-订单已结束', max_length=3, verbose_name='订单状态')),
                ('shopid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gb_account.Merchants', verbose_name='消费门店号')),
                ('spid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gb_merchant.Services', verbose_name='服务号')),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gb_account.Users', verbose_name='消费用户号')),
            ],
            options={
                'verbose_name': 'A类订单',
                'verbose_name_plural': 'A类订单',
            },
        ),
        migrations.CreateModel(
            name='BOrders',
            fields=[
                ('orderid', models.CharField(help_text='md5加密', max_length=32, primary_key=True, serialize=False, verbose_name='订单号')),
                ('oPhone', models.DecimalField(decimal_places=0, help_text='11位', max_digits=11, verbose_name='联系电话')),
                ('oPrice', models.DecimalField(decimal_places=2, help_text='0.00-99999.99元', max_digits=7, verbose_name='价格')),
                ('oTime', models.DateTimeField(verbose_name='预约时间')),
                ('oDesc', models.TextField(help_text='最大50位', max_length=50, verbose_name='订单备注')),
                ('qrCode', models.ImageField(upload_to=gb_order.models.Orders.order_qrcode_path, verbose_name='二维码')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='订单创建时间')),
                ('oStatus', models.CharField(choices=[('yxd', '用户已下单'), ('yzf', '用户已支付'), ('yjd', '商家已接单'), ('yjs', '订单已结束')], help_text='yxd-用户已下单 yzf-用户已支付 yjd-商家已接单 yjs-订单已结束', max_length=3, verbose_name='订单状态')),
                ('upFile', models.FileField(help_text='上传文件', upload_to=gb_order.models.BOrders.order_file_path, verbose_name='上传文件')),
                ('shopid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gb_account.Merchants', verbose_name='消费门店号')),
                ('spid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gb_merchant.Services', verbose_name='服务号')),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gb_account.Users', verbose_name='消费用户号')),
            ],
            options={
                'verbose_name': 'B类订单',
                'verbose_name_plural': 'B类订单',
            },
        ),
    ]
