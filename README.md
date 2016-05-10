![Respons-O-Matic Screenshot](https://dl.dropboxusercontent.com/u/18132950/respons-o-matic.png)

# Respons-O-Matic

Respons-O-Matic is a super-low-overhead way to preview your responsive designs, as you build them. All it really is is a single HTML page that loads a specified local resource inside some iframes. You don't even need to be running a webserver to use it!


## How does it work?

Respons-O-Matic uses [devices.css](http://marvelapp.github.io/devices.css/) from the clever folks at [Marvel](https://marvelapp.com) to display your HTML within the context of a few different devices. Each device layout simply surrounds an iframe which loads the content you specify. 

Because each iframe has a different height/width, basic mediaquery rules like `@media only screen and (min-width: 400px)` will be triggered, allowing you to simultaneously preview your deisgn in a few different scenarios.

There's obviously no magic going on here, I just thought I'd share something that helps me work faster, with less overhead. ([See FAQ below](#faq))

## Installation

There's no real install per se, but here's a few steps just in case. 

#### Get The Files

First, just download or clone this repository to your hard drive someplace.

#### Before Continuing

After you've got the repository, I recommend checking out the included sample real quick. Just head to your browser, choose "File > Open" and point it at `/path/to/index.html`.

#### Configuring Your Setup
Once you see how the files just load in the iframes, you get a pretty good idea what's going on here. So, to set it up for your content:

1. If you have a webserver that is already serving your mockups, just edit the `loc` variable in `index.html` to point to that location, then skip ahead to "Serving It Up"
2. If you have just static content, you can:
	1. Drop your content right in this directory (be careful not to overwrite `index.html`) -or-
	2. Continue to edit in your existing location
	3. Either way, just provide the on-disk path to your html as the location variable in `index.html`

(Note: If you are using relative URLs for assets, etc in your own directory, this last method may not work. I'm working on making a better server for you ASAP.)


## Serving It Up

#### Option 1
By default, once configured above, you don't need to serve anything. You can simply choose "File > Open" from your browser and point it at `/path/to/index.html` on your hard drive.

#### Option 2
If you have python installed, open up Terminal.app, then:

```
cd /path/to/responsomatic
python ./serveit.py
```

If you see an error that the script can't run, most likely you just need to `chmod 755 ./serveit.py`

If you see an error about the port (8080) already being in use then you can change it in the script, or &hellip;

#### Option 3
```
cd /path/to/responsomatic
python -m SimpleHTTPServer PORT_NUMBER
```

Where `PORT_NUMBER` is a port of your choosing.

## More To Come

I'm working on the following right now:

* ability to switch devices
* ability to switch between landscape and portrait
* a better serve script that will serve content form you project directory as a configuration parameter

What else? Feel free to add an [enhancement request](https://github.com/BenjaminListwon/responsomatic/issues) with your thoughts, or fork it and send a Pull Request my way.


<a name="faq"></a>

## Frequently Asked Questions

(Not really, I just made them up so I could answer some things in advance.)

#### Why does this exist?

While there are [loads of wonderful pieces of software](http://www.hongkiat.com/blog/rwd-tools/#testing) out there that let you preview RWD layouts in realtime. But if you're like me, the last thing you need / want is more tools in your toolchain. (Only Adam West had more tools in his belt than the modern web designer.) 

Besides, I got tired of always having to gulp my gulpfiles, pack my webpacks and vulcanize my &hellip; vulcans(?) before I could see results in the browser. Not to mention needing a whole [boatload of devices around](http://www.html5rocks.com/static/images/screenshots/crossdevice/image16.gif)

So, one day I figuresd I'd make something that &hellip;

* needs no special configuration
* needs no extra tools or libraries (npm, bower, gulp, etc)
* didn't (necessarily) need a webserver
* could be modified without compiling/recompiling
* was easily understood by anyone who wanted to see a demo
* allowed in-place use/reuse of work I was already doing
* could easily be used on several projects without even more configuration, etc
* can be used even when offline


#### But, but, but &hellip;

I can hear the collective chorus as I write this &hellip; 

* "There's no live reload!"
* "Those displays aren't actually at 1&times;, 2&times;, 3.1415&times;, 2&Sigma;<sub>1..n</sub>&times;, etc!"
* "What about Samsung?"

Again, there's loads of products out there. [Here's a handy chart](http://enigmatic-tor-1148.herokuapp.com/) of some of those tools made by [kdimatteo](https://github.com/kdimatteo) for example. 

Respons-O-Matic is not intended to replace any of them, or to even approximate anything like actual on-device testing.


#### Which tool would you use for that then?

Alas, I don't know enough about any RWD preview tool or testing framework to speak intelligently about the subject, or to recommend one. 


#### Isn't this the same as XYZ?

Sure. Here's [one](https://github.com/mattkersley/Responsive-Design-Testing) and a [search](https://www.google.com/webhp?#newwindow=1&q=responsive+design+testing) will show you loads more. I encourage you to shop around for the one that fits your needs and workflow the best.

#### What's with the name "r-o-m-assets"?

I wanted an assets directory that was likely to not be overwritten when someone drops their content into root folder. One less thing to worry about troubleshooting.

