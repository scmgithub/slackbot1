# check the token?  VGgoWiNMjlLy9J3JtOZxsn1r


quote="$(curl -s http://ron-swanson-quotes.herokuapp.com/v2/quotes)"
echo *${quote:1:${#quote}-2}* -R. Swanson


# bold the quote, add -R. Swanson