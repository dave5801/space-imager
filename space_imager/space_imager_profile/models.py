from django.db import models

'''
{
'copyright': 'Damian Peach', 
'date': '2018-01-12', 
'explanation': "Discovered with the PanSTARRS telescope on September 7, 2016, this Comet PanSTARRS, C/2016 R2, is presently about 24 light minutes (3 AU) from the Sun, sweeping through planet Earth's skies across the background of stars in the constellation Taurus. An inbound visitor from our Solar System's distant Oort Cloud, its beautiful and complex ion tail is a remarkable shade of blue. Still relatively far from the Sun, the comet's already well-developed ion tail is very impressive. Emission from unusually abundant ionized carbon monoxide (CO+) molecules fluorescing in the increasing sunlight is largely responsible for the pretty blue tint. This color image of the blue comet is a combination of data taken from two different telescopes during the night of January 7. Located at the apex of the V-shaped Hyades star cluster in Taurus, bright star Gamma Tauri is responsible for the glow at the bottom left corner of the frame.",
'hdurl': 'https://apod.nasa.gov/apod/image/1801/c2016_r2_2018_01_07dpjjc.jpg', 
'media_type': 'image', 
'service_version': 'v1', 
'title': 'Blue Comet PanSTARRS', 
'url': 'https://apod.nasa.gov/apod/image/1801/c2016_r2_2018_01_07dpjjc1024.jpg'
}
'''

class Space_Image(models.Model):
    """Model for a Space Photo."""
    copyright = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now=True)
    explanation = models.TextField(max_length=2000)
    hdurl = models.CharField(max_length=180)
    media_type = models.TextField(max_length=50)
    service_version = models.CharField(max_length=2)
    title = models.TextField(max_length=50)
    url = models.CharField(max_length=180)
