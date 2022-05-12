headTemplate = '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <title>ACES VWG ODT - Compare Images </title>
    <style>
        * {
            margin: auto;
            padding: 0;
            text-align: center;
        }
    </style>
</head>

<body>

    <style>
        a.jx-knightlab div.knightlab-logo {
            visibility: hidden;
            display: none;
        }
        a.jx-knightlab span.juxtapose-name {
            /* visibility: hidden; */
            display: none;
        }
        div.jx-slider {
            color: #f70d8a;
        }
        div.jx-image div.jx-label {
            background-color: #f70d8a;
            opacity:1;
            color:#000000;
        }

        h1  {
        padding: 10px;
        font-weight: 300;
        }

        .grid-container {
        display: grid;
        grid-template-columns: COLUMN_BLOCK;
        grid-gap: 10px;
        }
    #juxtapose-wrapper {
      border: 10px solid #f70d8a;
    }
    </style>
    <!-- Title section -->
    <div class="title">
        <h1>HEADINGBLOCK</h1>
        Only tested and known to work on a Pro Display XDR in Chrome under MacOS 12.3
        <br>
        <br>
    
    <div  class="grid-container" id="compares" style="width:90%;background-color:transparent;">
'''


divTemplateSDRvsHDR = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate A revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="A - SDR" />
            <img src="images/ACES_ODT_Candidate A revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="A - HDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate B revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="B - SDR" />
            <img src="images/ACES_ODT_Candidate B revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="B - HDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate C revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="C - SDR" />
            <img src="images/ACES_ODT_Candidate C revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="C - HDR"  />
        </div>'''

divTemplateZvsHDR = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate A revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="A - HDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate B revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="B - HDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate C revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="C - HDR"  />
        </div>'''

divTemplateZvsSDR = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate A revRRR - SDRsim.XXXX.avif"  loading="lazy" data-label="A - SDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate B revRRR - SDRsim.XXXX.avif"  loading="lazy" data-label="B - SDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate C revRRR - SDRsim.XXXX.avif"  loading="lazy" data-label="C - SDR"  />
        </div>'''

divTemplateAvsC = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate A revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="A - SDR" />
            <img src="images/ACES_ODT_Candidate C revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="C - SDR" />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate A revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="A - HDR"  />
            <img src="images/ACES_ODT_Candidate C revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="C - HDR"  />
        </div>'''

divTemplateBvsC = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate B revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="B - SDR" />
            <img src="images/ACES_ODT_Candidate C revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="C - SDR" />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate B revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="B - HDR"  />
            <img src="images/ACES_ODT_Candidate C revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="C - HDR"  />
        </div>'''

divTemplateAvsB = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate A revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="A - SDR" />
            <img src="images/ACES_ODT_Candidate B revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="B - SDR" />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate A revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="A - HDR"  />
            <img src="images/ACES_ODT_Candidate B revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="B - HDR"  />
        </div>'''

divTemplateYvsC = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate Y revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="ACES 1.3 - SDR" />
            <img src="images/ACES_ODT_Candidate C revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="C - SDR" />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="images/ACES_ODT_Candidate Y revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="ACES 1.3 - HDR"  />
            <img src="images/ACES_ODT_Candidate C revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="C - HDR"  />
        </div>'''


footTemplate = '''    </div>
    <script
        src="js/juxtapose.min.js">
    </script>
    <link rel="stylesheet"
        href="css/juxtapose.css">
    <link rel="stylesheet" type="text/css"
        href="css/styles.css">
    <link rel="stylesheet" href="https://use.typekit.net/cbm8egl.css">
</body>

</html>'''



rev = '008'

## get list of image names from image directory
import os
imageNames = os.listdir('../docs/avifFrames')
## isolate frame numbers from name
frameNumbers = [x.split('.')[-2] for x in imageNames]
## sort frame numbers
frameNumbers.sort()
## remove duplicates
frameNumbers = list(dict.fromkeys(frameNumbers))
frameNumbers = [x for x in frameNumbers if x != '']

for frame in frameNumbers:
    print(frame)

############################################

# ### Write out SDR vs HDR
# newDivs = []
# description = 'ACES 2.0 OT Candidates revRRR - SDR vs HDR'.replace('RRR', rev)
# for frame in frameNumbers:
#     # print(str(i).zfill(4))
#     newDivs.append(divTemplateSDRvsHDR.replace('XXXX', frame).replace('RRR', rev))

# # for div in newDivs:
# #     print(div)

# #write to html file on disk
# with open('sdrVsHdr.html', 'w') as f:
#     f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','33% 33% 33%'))
#     f.write('\n'.join(newDivs))
#     f.write(footTemplate)

# ############################################

# ### Write out Matrix + EOTF vs HDR
# newDivs = []
# description = 'ACES 2.0 OT Candidates revRRR - Matrix + EOTF vs HDR'.replace('RRR', rev)
# for frame in frameNumbers:
#     # print(str(i).zfill(4))
#     newDivs.append(divTemplateZvsHDR.replace('XXXX', frame).replace('RRR', rev))

# # for div in newDivs:
# #     print(div)

# #write to html file on disk
# with open('MatrixEOTFvsHDR.html', 'w') as f:
#     f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','33% 33% 33%'))
#     f.write('\n'.join(newDivs))
#     f.write(footTemplate)

# ############################################

# ### Write out Matrix + EOTF vs SDR
# newDivs = []
# description = 'ACES 2.0 OT Candidates revRRR - Matrix + EOTF vs SDR'.replace('RRR', rev)
# for frame in frameNumbers:
#     # print(str(i).zfill(4))
#     newDivs.append(divTemplateZvsSDR.replace('XXXX', frame).replace('RRR', rev))

# # for div in newDivs:
# #     print(div)

# #write to html file on disk
# with open('MatrixEOTFvsSDR.html', 'w') as f:
#     f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','33% 33% 33%'))
#     f.write('\n'.join(newDivs))
#     f.write(footTemplate)


# ############################################

# ### Write out A vs C
# newDivs = []
# description = 'ACES 2.0 OT Candidates revRRR - A vs C'.replace('RRR', rev)
# for frame in frameNumbers:
#     # print(str(i).zfill(4))
#     newDivs.append(divTemplateAvsC.replace('XXXX', frame).replace('RRR', rev))

# for div in newDivs:
#     print(div)

# #write to html file on disk
# with open('AvsC.html', 'w') as f:
#     f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','50% 50%'))
#     f.write('\n'.join(newDivs))
#     f.write(footTemplate)

# ############################################

# ### Write out A vs B
# newDivs = []
# description = 'ACES 2.0 OT Candidates revRRR - A vs B'.replace('RRR', rev)
# for frame in frameNumbers:
#     # print(str(i).zfill(4))
#     newDivs.append(divTemplateAvsB.replace('XXXX', frame).replace('RRR', rev))

# for div in newDivs:
#     print(div)

# #write to html file on disk
# with open('AvsB.html', 'w') as f:
#     f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','50% 50%'))
#     f.write('\n'.join(newDivs))
#     f.write(footTemplate)

# ############################################

# ### Write out B vs C
# newDivs = []
# description = 'ACES 2.0 OT Candidates revRRR - B vs C'.replace('RRR', rev)
# for frame in frameNumbers:
#     # print(str(i).zfill(4))
#     newDivs.append(divTemplateBvsC.replace('XXXX', frame).replace('RRR', rev))

# for div in newDivs:
#     print(div)

# #write to html file on disk
# with open('BvsC.html', 'w') as f:
#     f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','50% 50%'))
#     f.write('\n'.join(newDivs))
#     f.write(footTemplate)

# ############################################

# ### Write out Y vs C
# newDivs = []
# description = 'ACES 2.0 OT Candidates revRRR - 1.2 vs C'.replace('RRR', rev)
# for frame in frameNumbers:
#     # print(str(i).zfill(4))
#     newDivs.append(divTemplateYvsC.replace('XXXX', frame).replace('RRR', rev))

# for div in newDivs:
#     print(div)

# #write to html file on disk
# with open('YvsC.html', 'w') as f:
#     f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','50% 50%'))
#     f.write('\n'.join(newDivs))
#     f.write(footTemplate)



def writeComparisonPage(pagename,description,columns,comparisons):
    divTemplateSingle = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">
            <img src="avifFrames/ACES_ODT_Candidate CAND_L revRRR - TYPE_L.XXXX.avif"    loading="lazy" data-label="LABEL_L" />
            <img src="avifFrames/ACES_ODT_Candidate CAND_R revRRR - TYPE_R.XXXX.avif"    loading="lazy" data-label="LABEL_R" />
        </div>
  '''
    newDivs = []
    description = description.replace('RRR', rev)
    for frame in frameNumbers:
        # print(str(i).zfill(4))
        for i,comparison in enumerate(comparisons):
            print(comparison)
            newDiv = divTemplateSingle.replace('RRR', rev)
            newDiv = newDiv.replace('CAND_L',comparisons[i][0][0])
            newDiv = newDiv.replace('CAND_R',comparisons[i][1][0])
            newDiv = newDiv.replace('TYPE_L',comparisons[i][0][1])
            newDiv = newDiv.replace('TYPE_R',comparisons[i][1][1])
            newDiv = newDiv.replace('XXXX',frame)
            newDiv = newDiv.replace('LABEL_L',comparisons[i][0][2])
            newDiv = newDiv.replace('LABEL_R',comparisons[i][1][2])
            # print(newDiv)
            newDivs.append(newDiv)

    for div in newDivs:
        print(div)

    #write to html file on disk
    with open(pagename, 'w') as f:
        f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK',columns))
        f.write('\n'.join(newDivs))
        f.write(footTemplate)

# writeComparisonPage(pagename,description,columns,comparisons)



writeComparisonPage(\
pagename = '../docs/CurrentvsA.html',\
description = 'ACES 2.0 OT Candidates revRRR - 1.3 vs A'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['Y','SDRsim','ACES 1.3 SDR'],['A','SDRsim','A SDR']],[['Y','Rec.2100','ACES 1.3 HDR'],['A','Rec.2100','A HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/CurrentvsB.html',\
description = 'ACES 2.0 OT Candidates revRRR - 1.3 vs B'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['Y','SDRsim','ACES 1.3 SDR'],['B','SDRsim','B SDR']],[['Y','Rec.2100','ACES 1.3 HDR'],['B','Rec.2100','B HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/CurrentvsC.html',\
description = 'ACES 2.0 OT Candidates revRRR - 1.3 vs C'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['Y','SDRsim','ACES 1.3 SDR'],['C','SDRsim','C SDR']],[['Y','Rec.2100','ACES 1.3 HDR'],['C','Rec.2100','C HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/AvsB.html',\
description = 'ACES 2.0 OT Candidates revRRR - A vs B'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['A','SDRsim','A SDR'],['B','SDRsim','B SDR']],[['A','Rec.2100','A HDR'],['B','Rec.2100','B HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/AvsC.html',\
description = 'ACES 2.0 OT Candidates revRRR - A vs C'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['A','SDRsim','A SDR'],['C','SDRsim','C SDR']],[['A','Rec.2100','A HDR'],['C','Rec.2100','C HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/BvsC.html',\
description = 'ACES 2.0 OT Candidates revRRR - B vs C'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['B','SDRsim','B SDR'],['C','SDRsim','C SDR']],[['B','Rec.2100','B HDR'],['C','Rec.2100','C HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/A.html',\
description = 'ACES 2.0 OT Candidates revRRR - A'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['A','SDRsim','A SDR'],['A','Rec.2100','A HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/B.html',\
description = 'ACES 2.0 OT Candidates revRRR - B'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['B','SDRsim','B SDR'],['B','Rec.2100','B HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/C.html',\
description = 'ACES 2.0 OT Candidates revRRR - C'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['C','SDRsim','C SDR'],['C','Rec.2100','C HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/Y.html',\
description = 'ACES 2.0 OT Candidates revRRR - ACES 1.3'.replace('RRR', rev),\
columns = '50% 50%',\
comparisons = [[['Y','SDRsim','ACES 1.3 SDR'],['Y','Rec.2100','ACES 1.3 HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/MatrixEOTFvsHDR.html',\
description = 'ACES 2.0 OT Candidates revRRR - Matrix + EOTF vs HDR'.replace('RRR', rev),\
columns = '33% 33% 33%',\
comparisons = [[['Z','Rec.2100','Matrix + EOTF'],['A','Rec.2100','A HDR']],[['Z','Rec.2100','Matrix + EOTF'],['B','Rec.2100','B HDR']],[['Z','Rec.2100','Matrix + EOTF'],['C','Rec.2100','C HDR']]],\
)

writeComparisonPage(\
pagename = '../docs/MatrixEOTFvsSDR.html',\
description = 'ACES 2.0 OT Candidates revRRR - Matrix + EOTF vs SDR'.replace('RRR', rev),\
columns = '33% 33% 33%',\
comparisons = [[['Z','Rec.2100','Matrix + EOTF'],['A','SDRsim','A SDR']],[['Z','Rec.2100','Matrix + EOTF'],['B','SDRsim','B SDR']],[['Z','Rec.2100','Matrix + EOTF'],['C','SDRsim','C SDR']]],\
)

writeComparisonPage(\
pagename = '../docs/sdrVsHdr.html',\
description = 'ACES 2.0 OT Candidates revRRR - SDR vs HDR'.replace('RRR', rev),\
columns = '33% 33% 33%',\
comparisons = [[['A','SDRsim','A SDR'],['A','Rec.2100','A HDR']],[['B','SDRsim','B SDR'],['B','Rec.2100','B HDR']],[['C','SDRsim','C SDR'],['C','Rec.2100','C HDR']]],\
)

