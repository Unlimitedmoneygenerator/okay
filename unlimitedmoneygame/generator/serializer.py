from rest_framework import serializers



from .models import Playing, black, Game, Ticket, Modifiers,Trade,Inventory,TradeSpace,LuckCalc,Chat,User,Invoice,KeySeed,APIKEY

class APIListSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKEY
        fields = (
            "KEY",
            

            
        )
class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playing
        fields = (
            "p_name",
            "p_level",

            
        )

class KeyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeySeed
        fields = (
            "p_namer",
            "p_timer",
            "p_keyseed",
            "p_activated"

            
        )

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            "username",
            "pay_amount",
            "amount_received",
            "address",
            "p_timer",
            "payment_status",
            "price_amount",
            "p_qrcode"
        )

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playing
        fields = (
            "p_name",
            "p_id",
            "p_money",
            "p_luck",
            "p_level",
            "p_orders",
            "p_exp",
            "p_trades",
            "p_forceluck",
            "p_playing"

            
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "username",
            "id",
            "password" 
        )
        extra_kwargs = {
            'password': {'write only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifiers
        fields = (
        "sores",
        "umgtax",
        "winnersplit",
        "soresplit",
        "baseluck",
        "baseforceluck"

            
        )

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
        "p_name",
        "p_level",
        "p_content",
        "p_restricted",

            
        )

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "p_name",
            "p_amount",
            "p_class"
            

            
        )
class TradeFalseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = (
            "secp_name", #who trade is from
            "accepted",
            "p_name"
            
            
        )

class FLSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = (
            "downtwenty",
            
            
        )

class FLTWOSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downforty",
            
            
        )
class FLTHREESerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downeighty",
            
            
        )
class FLFOURSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downsixteen",
            
            
        )
class FLFIVESerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downthirtytwo",
            
            
        )
class FLSIXSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downthirtythree",
            
            
        )
    

class AcceptedTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = (
        "p_active",
        "fp_accepted",
        "secp_name",
        "secp_accepted",
        "middlestack",
        "fpstack",
        "spstack",
        "accepted",
        "p_name",
        "secp_name", #who trade is from
        "accepted"

            
        )


class PlayerSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playing
        fields = (
            "p_name", #who trade is from
            "p_level"

            
        )
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            "seasontime",
            "seasonseed",
            "roundtime",
            "roundseed",
            "roundcounter",

            
        )

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            "s_rarity",
            "s_cooldown",
            "s_name",
            "s_status",
            "s_durability",
            "p_name"
            

            
        )


class TradeSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeSpace
        fields = (
            "s_rarity",
            "s_cooldown",
            "s_name",
            "s_status",
            "s_durability",
            "p_name"
            
        )

