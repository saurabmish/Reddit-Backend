echo "####    INCREMENTING JENNIFER'S KARMA ...    ####"
echo ""

curl --request PATCH \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    http://127.0.0.1:6500/api/v2/user/Jennifer/karma/increment

echo "####    JENNIFER'S KARMA INCREMENTED SUCCESSFULLY!!    ####"
echo ""
echo ""
echo "####    DECREMENTING HANNAH'S KARMA ...    ####"
echo ""

curl --request PATCH \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    http://127.0.0.1:6500/api/v2/user/Hannah/karma/decrement

echo "####    HANNAH'S KARMA DECREMENTED SUCCESSFULLY!!    ####"
echo ""
