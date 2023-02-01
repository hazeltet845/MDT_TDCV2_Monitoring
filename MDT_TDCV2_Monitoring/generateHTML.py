#author: Ethan Hazelton

import argparse
import os
import shutil

def collectROOTFile():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", default=None, help="ROOT file name")
    return parser.parse_args()

def main():
    option = collectROOTFile()
    if not option.r:
        errorMsg("Please give the ROOT file name with -r")

    rootFile = str(option.r)
    #Home 
    template = "".join( open("./Template/HTML/home.html").readlines())
    fi = open("./Current/HTML/home.html", "w")
    fi.write( template % {"rootFile": rootFile } )
    fi.close()

    #Events
    template = "".join( open("./Template/HTML/events.html").readlines())
    fi = open("./Current/HTML/events.html", "w")
    fi.write( template % {"rootFile": rootFile } )
    fi.close()

    #Event Display
    template = "".join( open("./Template/HTML/event_display_passing.html").readlines())
    fi = open("./Current/HTML/event_display_passing.html", "w")
    fi.write( template % {"rootFile": rootFile } )
    fi.close()

    template = "".join( open("./Template/HTML/event_display_failing.html").readlines())
    fi = open("./Current/HTML/event_display_failing.html", "w")
    fi.write( template % {"rootFile": rootFile } )
    fi.close()

    #Global
    template = "".join( open("./Template/HTML/Global.html").readlines())
    fi = open("./Current/HTML/Global.html", "w")
    fi.write( template % {"rootFile": rootFile } )
    fi.close()

    #Channel Selection
    template = "".join( open("./Template/HTML/channels_selection.html").readlines())
    fi = open("./Current/HTML/channels_selection.html", "w")
    fi.write( template % {"rootFile": rootFile } )
    fi.close()

    #TDC pages
    for k in range(36):
        if k < 10:
            template = "".join( open("./Template/HTML/TDC/TDC0%s_TDC.html" % (k)).readlines())
            fi = open("./Current/HTML/TDC/TDC0%s_TDC.html" % (str(k)), "w")
            fi.write( template % {"rootFile": rootFile } )
            fi.close()

            template = "".join( open("./Template/HTML/TDC/TDC0%s_ADC.html" % (k)).readlines())
            fi = open("./Current/HTML/TDC/TDC0%s_ADC.html" % (str(k)), "w")
            fi.write( template % {"rootFile": rootFile } )
            fi.close()
        else:
            template = "".join( open("./Template/HTML/TDC/TDC%s_TDC.html" % (k)).readlines())
            fi = open("./Current/HTML/TDC/TDC%s_TDC.html" % (str(k)), "w")
            fi.write( template % {"rootFile": rootFile } )
            fi.close()

            template = "".join( open("./Template/HTML/TDC/TDC%s_ADC.html" % (k)).readlines())
            fi = open("./Current/HTML/TDC/TDC%s_ADC.html" % (str(k)), "w")
            fi.write( template % {"rootFile": rootFile } )
            fi.close()

    print("Generating TDCV2 Monitoring HTML with " + rootFile)

def errorMsg(message):
    import sys
    sys.exit("Fatal error: %s" % (message))

if __name__ == "__main__":
    main()