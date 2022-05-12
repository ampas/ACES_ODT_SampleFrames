
import sys
from subprocess import Popen
import os

pngDir = '/Users/afry/Working/ACES_ODT_Candidates_LUT_Render_v003/examplesPng/'
avifDir = '/Users/afry/GitHub/ACES_ODT_SampleFrames/docs/avifFrames'

pngFrames = os.listdir(pngDir)
pngFrames = [f for f in pngFrames if f.endswith('.png')]
pngFrames = sorted(pngFrames)

cicp_P = str(9)
cicp_T = str(16)
cicp_M = str(9)
cicp_string = '/'.join([cicp_P,cicp_T,cicp_M])

overWrite = False


for pngFrame in pngFrames:
    pngPath = os.path.join(pngDir, pngFrame)
    avifPath = os.path.join(avifDir, pngFrame.replace('.png', '.avif'))

    commandString = '/usr/local/bin/avifenc   -s 3 -j 12 --min 0 --max 10 -a end-usage=q -a cq-level=10 -a color:aq-mode=1 -a color:sharpness=2  -a color:enable-chroma-deltaq=1 -a color:qm-min=0 -a color:deltaq-mode=3  --cicp %s  \"%s\"  \"%s\"' % (cicp_string,pngPath,avifPath)
    print(commandString)
    

    #does avif exist?
    if os.path.isfile(avifPath) == False or overWrite == True:
        os.system(commandString)
        # proc = Popen([commandString], shell=False,
        #             stdin=None, stdout=None, stderr=None, close_fds=True)
        print('Done')
    