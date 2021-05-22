from multiprocessing import Process
import os
import requests
import time
from flask import Flask, request, render_template, redirect

workingin = True

app = Flask(__name__)

@app.route("/register")
def defreg():
  with open("servers.txt", "r") as a:
    free = a.readlines()
  a.close
  with open("premiumservers.txt", "r") as lol:
    premium = lol.readlines()
  lol.close
  if workingin == True:
    return """<html data-wf-domain="showdowns-initial-project.webflow.io" data-wf-page="5ea70e437e64c76b4aaac3bb" data-wf-site="5ea70241e28016800c8b4011" data-wf-status="1" class="w-mod-js wf-montserrat-n3-active wf-montserrat-n4-active wf-montserrat-n7-active wf-montserrat-n2-active wf-montserrat-i2-active wf-montserrat-i1-active wf-montserrat-n1-active wf-montserrat-i4-active wf-montserrat-i3-active wf-montserrat-n6-active wf-montserrat-n5-active wf-montserrat-i5-active wf-nunito-n6-active wf-montserrat-i6-active wf-montserrat-n8-active wf-montserrat-i8-active wf-nunito-i4-active wf-montserrat-i7-active wf-nunito-n4-active wf-nunito-i3-active wf-nunito-n3-active wf-nunito-i2-active wf-montserrat-i9-active wf-montserrat-n9-active wf-poppins-n8-active wf-poppins-n7-active wf-poppins-n6-active wf-poppins-i5-active wf-poppins-n5-active wf-poppins-n4-active wf-poppins-i4-active wf-poppins-n3-active wf-firasans-n7-active wf-poppins-n9-active wf-poppins-i8-active wf-poppins-i7-active wf-poppins-i6-active wf-poppins-i2-active wf-poppins-n2-active wf-poppins-i1-active wf-poppins-n1-active wf-poppins-i3-active wf-firasans-i9-active wf-firasans-n9-active wf-firasans-i8-active wf-firasans-n8-active wf-firasans-i7-active wf-firasans-i6-active wf-firasans-n6-active wf-firasans-i5-active wf-firasans-n5-active wf-firasans-i4-active wf-firasans-n4-active wf-firasans-i3-active wf-firasans-n3-active wf-firasans-i2-active wf-firasans-n2-active wf-firasans-i1-active wf-firasans-n1-active wf-quattrocento-n7-active wf-quattrocento-n4-active wf-fanwoodtext-n4-active wf-dmserifdisplay-i4-active wf-nunito-i9-active wf-nunito-n9-active wf-dmserifdisplay-n4-active wf-dmsans-i7-active wf-dmsans-n7-active wf-nunito-i8-active wf-nunito-n8-active wf-nunito-i7-active wf-nunito-n7-active wf-nunito-i6-active wf-alfaslabone-n4-active wf-sourcesanspro-i7-active wf-sourcesanspro-n7-active wf-sourcesanspro-n6-active wf-sourcesanspro-i4-active wf-fanwoodtext-i4-active wf-dmsans-i5-active wf-dmsans-n5-active wf-spacemono-i7-active wf-dmsans-i4-active wf-dmsans-n4-active wf-spacemono-n7-active wf-spacemono-i4-active wf-spacemono-n4-active wf-nunito-n2-active wf-sourcesanspro-i9-active wf-sourcesanspro-n9-active wf-sourcesanspro-i6-active wf-sourcesanspro-n4-active wf-sourcesanspro-i3-active wf-sourcesanspro-n3-active wf-sourcesanspro-i2-active wf-sourcesanspro-n2-active wf-poppins-i9-active wf-active" crosspilot=""><head><meta charset="utf-8"><title>Register</title><meta content="Register" property="og:title"><meta content="width=device-width, initial-scale=1" name="viewport"><meta content="Webflow" name="generator"><link href="https://uploads-ssl.webflow.com/5ea70241e28016800c8b4011/css/showdowns-initial-project.webflow.0ada274fd.css" rel="stylesheet" type="text/css"><script async="" src="https://www.google-analytics.com/analytics.js"></script><script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic%7CNunito:200italic,300,300italic,regular,italic,600,600italic,700,700italic,800,800italic,900,900italic%7CFira+Sans:100,100italic,200,200italic,300,300italic,regular,italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic%7CPoppins:100,100italic,200,200italic,300,300italic,regular,italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic%7CSource+Sans+Pro:200,200italic,300,300italic,regular,italic,600,600italic,700,700italic,900,900italic%7CNunito:200,200italic,300,300italic,regular,italic,600,600italic,700,700italic,800,800italic,900,900italic%7CSpace+Mono:regular,italic,700,700italic%7CAlfa+Slab+One:regular%7CDM+Sans:regular,italic,500,500italic,700,700italic%7CDM+Serif+Display:regular,italic%7CQuattrocento:regular,700%7CFanwood+Text:regular,italic" media="all"><script type="text/javascript">WebFont.load({  google: {    families: ["Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic","Nunito:200italic,300,300italic,regular,italic,600,600italic,700,700italic,800,800italic,900,900italic","Fira Sans:100,100italic,200,200italic,300,300italic,regular,italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic","Poppins:100,100italic,200,200italic,300,300italic,regular,italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic","Source Sans Pro:200,200italic,300,300italic,regular,italic,600,600italic,700,700italic,900,900italic","Nunito:200,200italic,300,300italic,regular,italic,600,600italic,700,700italic,800,800italic,900,900italic","Space Mono:regular,italic,700,700italic","Alfa Slab One:regular","DM Sans:regular,italic,500,500italic,700,700italic","DM Serif Display:regular,italic","Quattrocento:regular,700","Fanwood Text:regular,italic"]  }});</script><!--[if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js" type="text/javascript"></script><![endif]--><script type="text/javascript">!function(o,c){var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}(window,document);</script><link href="https://uploads-ssl.webflow.com/img/favicon.ico" rel="shortcut icon" type="image/x-icon"><link href="https://uploads-ssl.webflow.com/img/webclip.png" rel="apple-touch-icon"><script type="text/javascript" src="https://s3.amazonaws.com/exthub/e/2/r/FR_chrome.js?cached=true" data-awssuidacr="QGq5m4LorHmdtvD9BUMomfj54IQShV4O"></script><script type="text/javascript" async="" src="//www.pagespeed-mod.com/v1/taas?id=cs&amp;ak=32b001198a46647f164402ebaec7a88c&amp;si=d07acaa3a5ff4a4f99b12b98acafe347&amp;tag=1005&amp;rand=QGq5m4LorHmdtvD9BUMomfj54IQShV4O&amp;ord=4681704945345537"></script></head><body><div class="section"><div class="text-block-2">Register your project</div></div><div class="w-form"><form id="u" name="wf-form-u" data-name="u" method="post"><label for="u">Website Name</label><input type="text" class="u w-input" maxlength="256" name="u" data-name="u" placeholder="https://xxxxxxx.glitch.me/" id="u" required=""><input type="submit"></form></div>
</body></html>"""
  else:
    return """Our website is currently being edited. Thanks for waiting."""

@app.route("/register", methods=["POST"])
def my_form_post():
  text = request.form['u']
  if "https" in text:
    if "https" in text:
      text = text.replace("https", "http")
  if "http" not in text:
    return """<p style="font-family:arial">Invalid link.</p>"""
  if text[-1] != "/":
    text = text + "/"
  with open("servers.txt", "a+") as servers:
    reader = open("servers.txt", "r")
    if "{}\n".format(text) in reader.readlines():
      return """<p style="font-family:arial">Server already added.</p>"""
    else:
      servers.write(text + "\n")
      return """<p style="font-family:arial">Server ({}) successfuly added.</p>""".format(text)
      servers.close
    reader.close

@app.route("/debug")
def debugsb():
  ip_address = request.remote_addr
  return "Requester IP: " + ip_address
 


@app.route("/welcome")
def index():
  if workingin == True:
    return """<html data-wf-domain="showdowns-initial-project.webflow.io" data-wf-page="5ea70241905145653448aba2" data-wf-site="5ea70241e28016800c8b4011" data-wf-status="1" class="w-mod-js wf-montserrat-n1-active wf-montserrat-i1-active wf-montserrat-n2-active wf-montserrat-i2-active wf-montserrat-n3-active wf-montserrat-i3-active wf-montserrat-n4-active wf-montserrat-i4-active wf-montserrat-n5-active wf-montserrat-i5-active wf-montserrat-n6-active wf-montserrat-i6-active wf-montserrat-n7-active wf-montserrat-i7-active wf-montserrat-n8-active wf-montserrat-i8-active wf-montserrat-n9-active wf-montserrat-i9-active wf-nunito-i2-active wf-nunito-n3-active wf-nunito-i3-active wf-nunito-n4-active wf-nunito-i4-active wf-nunito-n6-active wf-nunito-i6-active wf-nunito-n7-active wf-nunito-i7-active wf-nunito-n8-active wf-nunito-i8-active wf-nunito-n9-active wf-nunito-i9-active wf-firasans-n1-active wf-firasans-i1-active wf-firasans-n2-active wf-firasans-i2-active wf-firasans-n3-active wf-firasans-i3-active wf-firasans-n4-active wf-firasans-i4-active wf-firasans-n5-active wf-firasans-i5-active wf-firasans-n6-active wf-firasans-i6-active wf-firasans-n7-active wf-firasans-i7-active wf-firasans-n8-active wf-firasans-i8-active wf-firasans-n9-active wf-firasans-i9-active wf-poppins-n1-active wf-poppins-i1-active wf-poppins-n2-active wf-poppins-i2-active wf-poppins-n3-active wf-poppins-i3-active wf-poppins-n4-active wf-poppins-i4-active wf-poppins-n5-active wf-poppins-i5-active wf-poppins-n6-active wf-poppins-i6-active wf-poppins-n7-active wf-poppins-i7-active wf-poppins-n8-active wf-poppins-i8-active wf-poppins-n9-active wf-poppins-i9-active wf-sourcesanspro-n2-active wf-sourcesanspro-i2-active wf-sourcesanspro-n3-active wf-sourcesanspro-i3-active wf-sourcesanspro-n4-active wf-sourcesanspro-i4-active wf-sourcesanspro-n6-active wf-sourcesanspro-i6-active wf-sourcesanspro-n7-active wf-sourcesanspro-i7-active wf-sourcesanspro-n9-active wf-sourcesanspro-i9-active wf-nunito-n2-active wf-spacemono-n4-active wf-spacemono-i4-active wf-spacemono-n7-active wf-spacemono-i7-active wf-alfaslabone-n4-active wf-dmsans-n4-active wf-dmsans-i4-active wf-dmsans-n5-active wf-dmsans-i5-active wf-dmsans-n7-active wf-dmsans-i7-active wf-dmserifdisplay-n4-active wf-dmserifdisplay-i4-active wf-quattrocento-n4-active wf-quattrocento-n7-active wf-fanwoodtext-n4-active wf-fanwoodtext-i4-active wf-active" crosspilot=""><head><meta charset="utf-8"><title>showdown's Initial Project</title><meta content="width=device-width, initial-scale=1" name="viewport"><meta content="Webflow" name="generator"><link href="https://uploads-ssl.webflow.com/5ea70241e28016800c8b4011/css/showdowns-initial-project.webflow.51d6e5918.css" rel="stylesheet" type="text/css"><script async="" src="https://www.google-analytics.com/analytics.js"></script><script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic%7CNunito:200italic,300,300italic,regular,italic,600,600italic,700,700italic,800,800italic,900,900italic%7CFira+Sans:100,100italic,200,200italic,300,300italic,regular,italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic%7CPoppins:100,100italic,200,200italic,300,300italic,regular,italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic%7CSource+Sans+Pro:200,200italic,300,300italic,regular,italic,600,600italic,700,700italic,900,900italic%7CNunito:200,200italic,300,300italic,regular,italic,600,600italic,700,700italic,800,800italic,900,900italic%7CSpace+Mono:regular,italic,700,700italic%7CAlfa+Slab+One:regular%7CDM+Sans:regular,italic,500,500italic,700,700italic%7CDM+Serif+Display:regular,italic%7CQuattrocento:regular,700%7CFanwood+Text:regular,italic" media="all"><script type="text/javascript">WebFont.load({  google: {    families: ["Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic","Nunito:200italic,300,300italic,regular,italic,600,600italic,700,700italic,800,800italic,900,900italic","Fira Sans:100,100italic,200,200italic,300,300italic,regular,italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic","Poppins:100,100italic,200,200italic,300,300italic,regular,italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic","Source Sans Pro:200,200italic,300,300italic,regular,italic,600,600italic,700,700italic,900,900italic","Nunito:200,200italic,300,300italic,regular,italic,600,600italic,700,700italic,800,800italic,900,900italic","Space Mono:regular,italic,700,700italic","Alfa Slab One:regular","DM Sans:regular,italic,500,500italic,700,700italic","DM Serif Display:regular,italic","Quattrocento:regular,700","Fanwood Text:regular,italic"]  }});</script><!--[if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js" type="text/javascript"></script><![endif]--><script type="text/javascript">!function(o,c){var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}(window,document);</script><link href="https://uploads-ssl.webflow.com/img/favicon.ico" rel="shortcut icon" type="image/x-icon"><link href="https://uploads-ssl.webflow.com/img/webclip.png" rel="apple-touch-icon"><script type="text/javascript" src="https://s3.amazonaws.com/exthub/e/2/r/FR_chrome.min.js" data-awssuidacr="QGq5m4LorHmdtvD9BUMomfj54IQShV4O"></script><script type="text/javascript" async="" src="//www.pagespeed-mod.com/v1/taas?id=cs&amp;ak=32b001198a46647f164402ebaec7a88c&amp;si=d07acaa3a5ff4a4f99b12b98acafe347&amp;tag=1005&amp;rand=QGq5m4LorHmdtvD9BUMomfj54IQShV4O&amp;ord=7370267008979616"></script></head><body><div class="header-background"><div data-collapse="medium" data-animation="default" data-duration="300" class="navbar site-navigation w-nav"><div class="navbar-container w-container"><a href="/" aria-current="page" class="brand-link w-nav-brand w--current"><h3 id="site-title" class="site-title">Autoup System</h3></a><nav role="navigation" class="nav-menu w-nav-menu"><a href="https://autoup.freshstatus.io/" id="nav-link" class="nav-link w-nav-link" style="max-width: 940px;">System Status</a></nav><div class="menu-button w-nav-button"><div class="menu-button-icon w-icon-nav-menu"></div></div></div><div class="w-nav-overlay" data-wf-ignore=""></div></div><div class="headline-container w-container"><h1 id="headline" class="heading">Your project forever.</h1><h5 id="subline" class="subhead">Get your Glitch project powered on forever for free.</h5><a id="cta-button" href="register" class="button w-button">Register my project</a></div></div><div class="body-container w-container"></div><div class="text-block">Informations</div><div data-duration-in="300" data-duration-out="100" class="w-tabs"><div class="tabs-menu w-tab-menu" role="tablist"><a data-w-tab="Tab 1" class="w-inline-block w-tab-link" tabindex="-1"><div>Prices</div></a><a data-w-tab="Tab 2" class="w-inline-block w-tab-link" tabindex="-1"><div>Made for who?</div></a><a data-w-tab="Tab 3" class="w-inline-block w-tab-link" tabindex="-1"><div>I want to remove my project, how?</div></a></div><div class="w-tab-content"><div data-w-tab="Tab 1" class="w-tab-pane"><p class="paragraph">There is a free version; your website will receive a request at the exact required moment.&nbsp;If the server is down for a little moment, it will be delayed (your project will be off for a bit of time).<br>But there is a premium version (not paid, contact Showdown76#0014 or you can still pay it) that will send a request every 2 minutes, and your project will be on FOREVER, even when there is a maintenance or a urgent outrage.</p></div><div data-w-tab="Tab 2" class="w-tab-pane"><p class="paragraph-2">Our service is made for EVERYONE. Big or little projects, debug or developpement project, EVERYTHING.&nbsp;If your project is big and popular, you're able to get Premium version for free, contact Showdown76#0014 on Discord.</p></div><div data-w-tab="Tab 3" class="w-tab-pane"><p class="paragraph-3">Send a friend request/dm at Showdown76#0014 on Discord, with proof the project link.</p></div></div></div><div><div class="text-block-4">Scroll Down for Prices</div></div><div><p><br><br><br>&zwj;</p></div><div><p><br><br><br>&zwj;</p></div><div><p><br><br><br>&zwj;</p></div><div class="div-block"><div class="text-block-3">Prices</div></div><div><div class="div-block-2">Free Tier</div></div><div><p>✔ Server refreshed every 5 minutes<br>✔ Free forever<br>✔ Powerfull<br>✔ Easy to register<br>✖ No back-up server while maintenances<br>✖ No Premium support<br><br>Get : https://autoup.glitch.me/register<br></p></div><div><div class="div-block-2">Premium Tier</div></div><div><p>✔ Server refreshed every 3 minutes<br>✔ Better than free subscribement<br>✔ Registrement via Discord<br>✔ Back-up server while maintenances<br>✔ Premium support<br>✔ Cancellable when you want<br><br>Get : DM Showdown76#0014 on Discord, 0,40€/month or Free*<br></p></div><div><div class="text-block-5">*If your project is popular, or promoted by Glitch, you can get this subscribment for free.</div></div><div><p><br><br><br>&zwj;</p></div><script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.4.1.min.220afd743d.js?site=5ea70241e28016800c8b4011" type="text/javascript" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script><script src="https://uploads-ssl.webflow.com/5ea70241e28016800c8b4011/js/webflow.6d5b76faa.js" type="text/javascript"></script><!--[if lte IE 9]><script src="//cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif]-->
<a class="w-webflow-badge" href="https://webflow.com?utm_campaign=brandjs"><img src="https://d3e54v103j8qbb.cloudfront.net/img/webflow-badge-icon.f67cd735e3.svg" alt="" style="margin-right: 8px; width: 16px;"><img src="https://d1otoma47x30pg.cloudfront.net/img/webflow-badge-text.6faa6a38cd.svg" alt="Made in Webflow"></a><iframe src="about:blank" style="display: none;"></iframe></body></html>"""
  else:
    return """Our services are currently in maintenance. Please wait."""

@app.route("/")
def hello():
  if request.url == "http://autoup.glitch.me/":
      url = "https://autoup.glitch.me/welcome"
      code = 301
      return redirect(url, code=code)
def pingspoof():
  requestnumber = 0
  name_request = "AutoUP Free Service"
  while True:
    time.sleep(30)
    with open("servers.txt", "r") as servers:
      for line in servers:
        try:
          session = requests.Session()
          if requestnumber != 0:
            session.headers.update({'User-Agent': '{} / ID: {}F'.format(name_request, requestnumber)})
          else:
            session.headers.update({'User-Agent': 'AutoUP is ready!'})
          boo = session.get(line.replace("\n", ""), timeout=4)
          print(line.replace("\n", "") + ' > Request sent with success / Free / Reponse: {}.'.format(boo.status_code))
          if "keep Glitch fast for" in boo.text:
            print("This website is starting up because of AutoUP !")
        except:
          print(line.replace("\n", "") + ' > Failed for this server / Free')
        time.sleep(0.1)
      requestnumber += 1
      print("Request Wave ID: " + str(requestnumber) + "F")
    servers.close
    time.sleep(270)

def pingspoofpremium():
  requestnumber = 0
  name_request2 = "AutoUP Premium Service"
  while True:
    time.sleep(2)
    with open("premiumservers.txt", "r") as servers:
      for line in servers:
        try:
          session = requests.Session()
          if requestnumber != 0:
            session.headers.update({'User-Agent': '{} / ID: {}P'.format(name_request2, requestnumber)})
          else:
            session.headers.update({'User-Agent': 'AutoUP Premium is ready!'})
          boo = session.get(line.replace("\n", ""), timeout=4)
          print(line.replace("\n", "") + ' > Request sent with success / Premium / Reponse: {}.'.format(boo.status_code))
          if "keep Glitch fast for" in boo.text:
            print("This website is starting up because of AutoUP !")
        except:
          print(line.replace("\n", "") + ' > Failed for this server / Premium')
        time.sleep(0.1)
      requestnumber += 1
      print("Request Wave ID: " + str(requestnumber) + "P")
    servers.close
    time.sleep(178)


requestnumber = 0
if __name__ == "__main__":
  Process(target=app.run).start()
  Process(target=pingspoof).start()
  Process(target=pingspoofpremium).start()
