import cv2

coins = cv2.imread('coins.jpg')
coins_gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test.jpg',coins_gray)