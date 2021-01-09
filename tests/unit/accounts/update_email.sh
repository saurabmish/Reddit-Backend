echo "####    UPDATING ADAM'S EMAIL ...    ####"
echo ""

curl --request PATCH \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
    {
        "userid": 1,
        "username": "Adam",
        "email": "adam_new@gmail.com",
        "karma": 1
    }' \
    http://127.0.0.1:6500/api/v2/user/update/Adam

echo "####    ADAM'S EMAIL UPDATED SUCCESSFULLY!!    ####"
echo ""
echo ""
echo "####    UPDATING JENNIFER'S EMAIL ...    ####"
echo ""

curl --request PATCH \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
    {
        "userid": 2,
        "username": "Jennifer",
        "email": "jennifer_g@gmail.com",
        "karma": 1
    }' \
    http://127.0.0.1:6500/api/v2/user/update/Jennifer

echo "####    JENNIFER'S EMAIL UPDATED SUCCESSFULLY!!    ####"
echo ""
