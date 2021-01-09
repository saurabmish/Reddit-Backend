echo "####    INCREMENTING ADAM'S KARMA ...    ####"
echo ""

curl --request PATCH \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "name": "Adam",
            "location": "Chicago",
            "gender": "M"
        }' \
    http://127.0.0.1:6500/api/v2/user/update/Adam

echo "####    ADAM'S KARMA INCREMENTED SUCCESSFULLY!!    ####"
echo ""
echo ""
echo "####    DECREMENTING JASON'S KARMA ...    ####"
echo ""

curl --request PATCH \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "name": "Jason",
            "location": "Laguna Hills",
            "gender": "M"
        }' \
    http://127.0.0.1:6500/api/v2/user/update/Jason

echo "####    JASON'S KARMA DECREMENTED SUCCESSFULLY!!    ####"
echo ""
