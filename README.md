# youtube-history
Finds what your most watched videos were each month on YouTube. 

Example output snippet:  
```
~~~may~~~
title:  Andy Shauf - "To You" (Full Album Stream)
freq:   10
title:  Andy Shauf - "Quite Like You"
freq:   9
title:  Andy Shauf - "The Magician"
freq:   7
   ~~~june~~~
title:  [MV] IU(아이유) _ BBIBBI(삐삐)
freq:   10
title:  Peach - Kevin Abstract
freq:   9
title:  [MV] IU(아이유) _ Palette(팔레트) (Feat. G-DRAGON)
freq:   7
   ~~~july~~~
title:  joji - thom
freq:   12
title:  Frank Ocean - White Ferrari
freq:   8
title:  Boyer
freq:   8
   ~~~august~~~
title:  YeYe - うんざりですよ（Official Music Video）
freq:   10
title:  Boy Bye - BROCKHAMPTON
freq:   10
title:  If You Pray Right - BROCKHAMPTON
freq:   10
```
## Setup
1. Download your youtube history [here](https://takeout.google.com/settings/takeout/custom/youtube?pli=1) as HTML.

2. Copy "watch-history.html" into root directory.

3. Run `python3 create_link_and_text.py`

4. Run `python3 analyse.py`

5. (May need to `pip install beautifulsoup4` if not installed already) 
