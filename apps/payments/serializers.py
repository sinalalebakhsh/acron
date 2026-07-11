# serializers for payments app, connected to the mock bank callback endpoint

# why import serializers from rest_framework? 
# because we are using DRF to build our API endpoints, 
# and DRF provides a powerful and,
# flexible way to serialize and deserialize data. 
# The serializers module provides classes,
# that help convert complex data types, such as Django models, 
# into native Python datatypes that can then be easily rendered into JSON, 
# XML or other content types. 
# It also provides validation and deserialization of input data.
from rest_framework import serializers

# what is InitiatePaymentSerializer?
# InitiatePaymentSerializer is a serializer class that defines the structure of the data
class InitiatePaymentSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()

# what is MockBankCallbackSerializer?
# MockBankCallbackSerializer is a serializer class,
# that defines the structure of the callback data from the mock bank
class MockBankCallbackSerializer(serializers.Serializer):
    transaction_id = serializers.UUIDField()
    is_successful = serializers.BooleanField(default=True, help_text="تیک بزنید تا پرداخت موفق شبیه‌سازی شود")



