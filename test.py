from clip_mosaic import ClipMosaic


clipper = ClipMosaic('testdata', True)
clipper.clip_by_shp('testdata/testrange.shp', 'test_clip.tif')