from startup._common_imports import *  # @UnusedWildImport
from diffcalc.gdasupport.minigda.scannable import ScannableMotionWithScannableFieldsBase  # @UnusedImport
from diffcalc.gdasupport.minigda.scannable import DummyPD
if not GDA:    
    import startup._demo
else:
#     import __main__  # @UnresolvedImport
    from __main__ import dd2th,ddth,denergy  # @UnresolvedImport
LOCAL_MANUAL = "http://confluence.diamond.ac.uk/pages/viewpage.action?pageId=31853413"
# Diffcalc i06-1
# ======== === 
# delta    dd2th
# eta      ddth
# chi      dummy
# phi      dummy


### Create dummy scannables ###
if GDA:  
    print("!!! Starting LIVE diffcalc with delta(dd2th), eta(ddth), chi(dummy), phi(dummy) and denergy.") 
    delta = dd2th
    eta = ddth
    en=denergy
    
else:   
    delta = Dummy('delta')
    eta = Dummy('eta')
    en = Dummy('en')
    en(1500)
    
chi = DummyPD('chi')
phi = DummyPD('phi')

_fourc = ScannableGroup('_fourc', (delta, eta, chi, phi))
en.level = 3
 
### Configure and import diffcalc objects ###
ESMTGKeV = 1
settings.hardware = ScannableHardwareAdapter(_fourc, en, ESMTGKeV)
settings.geometry = diffcalc.hkl.you.geometry.FourCircle()  # @UndefinedVariable
settings.energy_scannable = en
settings.axes_scannable_group= _fourc
settings.energy_scannable_multiplier_to_get_KeV = ESMTGKeV
 
from diffcalc.gdasupport.you import *  # @UnusedWildImport
 
if GDA:
    print("Running in GDA --- aliasing commands")
    alias_commands(globals())
 
# Load the last ub calculation used
lastub() 
if not GDA:
    demo = startup._demo.Demo(globals(), 'fourc')
