from behave import fixture, use_fixture
from pyspark.sql import SparkSession


@fixture
def spark_session(context):
    context.session = SparkSession.builder \
        .appName('behave') \
        .master('local') \
        .getOrCreate()
    return context.session


def before_tag(context, tag):
    if tag == 'fixture.spark.session':
        use_fixture(spark_session, context)
