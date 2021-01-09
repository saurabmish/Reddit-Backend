echo "####    UPDATING ADAM'S EMAIL ...    ####"
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

echo "####    ADAM'S EMAIL UPDATED SUCCESSFULLY!!    ####"
echo ""
echo ""
echo "####    UPDATING JASON'S EMAIL ...    ####"
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

echo "####    JASON'S EMAIL UPDATED SUCCESSFULLY!!    ####"
echo ""
