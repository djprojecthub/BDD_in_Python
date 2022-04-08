from behave import *
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

subscribers_struct = StructType([
    StructField("subscriber_id", IntegerType()),
    StructField("subscriber_name", StringType())
])

product_struct = StructType([
    StructField("subscriber_id", IntegerType()),
    StructField("product_name", StringType()),
    StructField("purchase_timestamp", LongType())
])

DIWAKAR_ID = 1
AKANSHA_ID = 2
PRODUCT_NAME = 'Perfume'
DIFFERENT_PRODUCT = 'Leather Shoes'


# function under test
def generate_recipient_list(subscribers, products):
    return


def add_subscriber(context, subscriber_id, subscriber_name):
    if 'subscribers' in context:
        context.subscribers.append([subscriber_id, subscriber_name])
    else:
        context.subscribers = [[subscriber_id, subscriber_name]]


def add_purchase(context, subscriber_id, product_name=PRODUCT_NAME, timestamp=1):
    if 'products' in context:
        context.products.append([subscriber_id, product_name, timestamp])
    else:
        context.products = [[subscriber_id, product_name, timestamp]]


@given(u'Diwakar purchased a product')
def add_customer_with_product(context):
    add_subscriber(context, DIWAKAR_ID, 'Diwakar')
    add_purchase(context, DIWAKAR_ID)


@given(u'Diwakar purchased another product')
def add_second_product_for_diwakar(context):
    add_purchase(context, DIWAKAR_ID, DIFFERENT_PRODUCT)


@given(u'Akansha bought no products')
def add_subscriber_without_product(context):
    add_subscriber(context, AKANSHA_ID, 'Akansha')


@when(u'we generate newsletter recipients')
def prepare_newsletter_recipients(context):
    if 'subscribers' in context:
        subscribers = context.spark.createDataFrame(context.subscribers, subscribers_struct)
    else:
        subscribers = context.spark.createDataFrame([], subscribers_struct)

    if 'products' in context:
        products = context.spark.createDataFrame(context.products, product_struct)
    else:
        products = context.spark.createDataFrame([], product_struct)

    context.result = generate_recipient_list(subscribers, products).cache()

    context.result.show()


def verify_recipient_with_product_only_once(context, subscriber_name):
    df = context.result
    if subscriber_name:
        only_one_person = df.filter((df['subscriber_name'] == subscriber_name) & (df['product_name'].isNotNull()))
    else:
        only_one_person = df.filter((df['subscriber_name'].isNull()) & (df['product_name'].isNotNull()))

    assert only_one_person.count() == 1


@then(u'Diwakar is on the list')
def verify_diwakar_with_product(context):
    verify_recipient_with_product_only_once(context, 'Diwakar')


@then(u'Diwakar is on the list only once')
def verify_diwakar_with_product(context):
    verify_recipient_with_product_only_once(context, 'Diwakar')


@then(u'Diwakar gets a message about the second purchase')
def verify_diwakar_with_second_product(context):
    df = context.result
    only_one_person = df.filter((df['subscriber_name'] == 'Diwakar') & (df['product_name'] == DIFFERENT_PRODUCT))
    assert only_one_person.count() == 1


@then(u'Akansha is not on the list')
def verify_no_akansha(context):
    df = context.result
    only_akansha = df.filter(df['subscriber_name'] == 'Akansha')
    assert only_akansha.count() == 0
