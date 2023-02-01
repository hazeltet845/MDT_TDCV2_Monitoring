This runs the ROOT file produced by each run of the TDC

To run this locally:

 First, make sure the chosen ROOT file is in the MDT_TDCV2_Monitoring/data/ by linking the data directory to wherever the ROOT files are. Additionally, make sure the reference root file that is used for comparison is named "reference.root"

 Use the cd command to enter the MDT_TDCV2_Monitoring directory

 To generate the html where 'XXX' is the ROOT file name:
        " cmdline$> python generateHTML.py -r XXX "

    Ex: "
            cmdline$> cd Desktop/MDT_TDCV2_Monitoring/
            cmdline$> python generateHTML.py -r Events.root
        "

  Then start a local server and open any HTML file in MDT_TDCV2_Monitoring/Current/HTML/ 

-- Reminder: When viewing the graphs on the live server, a graph can be enlarged by double clicking

Corrsponding HTML pages to different tabs:
--home.html => "Home"
--Global.html => "Global"
--events.html => "Events"
--event_display_failing.html and event_display_passing.html => "Event Display"
--channels_selection.html => "Channel Selection"
--TDC pages => "TDC"