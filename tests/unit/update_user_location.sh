echo "####    UPDATING ADAM'S ADDRESS ...    ####"
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
    http://127.0.0.1:6500/api/v1/user/update-location/Adam

echo "####    ADAM'S ADDRESS UPDATED SUCCESSFULLY!!    ####"
echo ""
echo "####    UPDATING JASON'S ADDRESS ...    ####"
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
    http://127.0.0.1:6500/api/v1/user/update-location/Jason

echo "####    JASON'S ADDRESS UPDATED SUCCESSFULLY!!    ####"
echo ""
