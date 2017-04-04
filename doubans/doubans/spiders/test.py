import urlparse


url = 'https://www.douban.com/misc/captcha?id=uS4cbcp9SPW23nDpGRGcnkYH:en&size=s'

captcha_id = urlparse.parse_qs(urlparse.urlparse(url).query,True)['id'][0]

print captcha_id