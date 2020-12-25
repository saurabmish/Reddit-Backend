echo "####    DELETING USER JASON ...    ####"
echo ""

curl --request DELETE \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    http://127.0.0.1:6500/api/v1/user/delete/Jason

echo "####    USER JASON DELETED SUCCESFULLY!!    ####"
echo ""
