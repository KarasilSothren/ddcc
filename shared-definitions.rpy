# Definitions for extra audio channels
# Added by SuperHatGuy#1795

renpy.music.register_channel("music2", mixer="music", loop=True, tight=True)
renpy.music.register_channel("music3", mixer="music", loop=True, tight=True)
renpy.music.register_channel("sound2", mixer="sfx", loop=False, tight=False)
renpy.music.register_channel("sound3", mixer="sfx", loop=False, tight=False)
renpy.music.register_channel("voice2", mixer="voice", loop=False, tight=False)
renpy.music.register_channel("voice3", mixer="voice", loop=False, tight=False)

# Definitions for Main Character
# Sprites by Childish-N
# Definitions Compiled by CPG Yuri
# https://www.deviantart.com/childish-n/art/DDLC-Protagonist-Sprite-Version-2-751332184

#Character Definitions
define imc = Character('MC', image='mc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

image mc 1 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 1a = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 1b = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/b.png")
image mc 1c = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/c.png")
image mc 1d = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/d.png")
image mc 1e = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/e.png")
image mc 1f = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/f.png")
image mc 1g = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/g.png")
image mc 1h = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/h.png")
image mc 1i = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/i.png")
image mc 1j = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/j.png")
image mc 1k = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/k.png")
image mc 1l = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/l.png")
image mc 1m = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/m.png")
image mc 1n = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/n.png")
image mc 1o = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/o.png")
image mc 1p = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/p.png")
image mc 1q = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/q.png")
image mc 1r = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/r.png")
image mc 1s = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/s.png")
image mc 1t = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/t.png")
image mc 1u = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/u.png")
image mc 1v = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/v.png")
image mc 1w = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/w.png")
image mc 1x = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/x.png")
image mc 1y = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/y.png")
image mc 1z = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/z.png")
image mc 1error = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/error.png")
image mc 1error1 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/error1.png")
image mc 1shock = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/shock.png")

image mc 2 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 2a = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 2b = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/b.png")
image mc 2c = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/c.png")
image mc 2d = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/d.png")
image mc 2e = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/e.png")
image mc 2f = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/f.png")
image mc 2g = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/g.png")
image mc 2h = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/h.png")
image mc 2i = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/i.png")
image mc 2j = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/j.png")
image mc 2k = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/k.png")
image mc 2l = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/l.png")
image mc 2m = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/m.png")
image mc 2n = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/n.png")
image mc 2o = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/o.png")
image mc 2p = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/p.png")
image mc 2q = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/q.png")
image mc 2r = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/r.png")
image mc 2s = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/s.png")
image mc 2t = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/t.png")
image mc 2u = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/u.png")
image mc 2v = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/v.png")
image mc 2w = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/w.png")
image mc 2x = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/x.png")
image mc 2y = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/y.png")
image mc 2z = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/z.png")
image mc 2error = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/error.png")
image mc 2error1 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/error1.png")
image mc 2shock = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/1l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/shock.png")

image mc 3 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 3a = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 3b = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/b.png")
image mc 3c = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/c.png")
image mc 3d = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/d.png")
image mc 3e = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/e.png")
image mc 3f = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/f.png")
image mc 3g = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/g.png")
image mc 3h = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/h.png")
image mc 3i = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/i.png")
image mc 3j = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/j.png")
image mc 3k = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/k.png")
image mc 3l = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/l.png")
image mc 3m = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/m.png")
image mc 3n = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/n.png")
image mc 3o = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/o.png")
image mc 3p = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/p.png")
image mc 3q = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/q.png")
image mc 3r = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/r.png")
image mc 3s = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/s.png")
image mc 3t = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/t.png")
image mc 3u = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/u.png")
image mc 3v = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/v.png")
image mc 3w = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/w.png")
image mc 3x = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/x.png")
image mc 3y = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/y.png")
image mc 3z = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/z.png")
image mc 3error = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/error.png")
image mc 3error1 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/error1.png")
image mc 3shock = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/1r.png", (0, 0), "mod_assets/shared_assets/mc/shock.png")

image mc 4 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 4a = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 4b = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/b.png")
image mc 4c = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/c.png")
image mc 4d = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/d.png")
image mc 4e = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/e.png")
image mc 4f = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/f.png")
image mc 4g = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/g.png")
image mc 4h = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/h.png")
image mc 4i = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/i.png")
image mc 4j = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/j.png")
image mc 4k = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/k.png")
image mc 4l = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/l.png")
image mc 4m = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/m.png")
image mc 4n = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/n.png")
image mc 4o = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/o.png")
image mc 4p = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/p.png")
image mc 4q = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/q.png")
image mc 4r = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/r.png")
image mc 4s = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/s.png")
image mc 4t = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/t.png")
image mc 4u = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/u.png")
image mc 4v = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/v.png")
image mc 4w = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/w.png")
image mc 4x = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/x.png")
image mc 4y = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/y.png")
image mc 4z = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/z.png")
image mc 4error = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/error.png")
image mc 4error1 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/error1.png")
image mc 4shock = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/2l.png", (0, 0), "mod_assets/shared_assets/mc/2r.png", (0, 0), "mod_assets/shared_assets/mc/shock.png")

image mc 5 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 5a = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/a.png")
image mc 5b = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/b.png")
image mc 5c = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/c.png")
image mc 5d = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/d.png")
image mc 5e = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/e.png")
image mc 5f = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/f.png")
image mc 5g = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/g.png")
image mc 5h = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/h.png")
image mc 5i = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/i.png")
image mc 5j = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/j.png")
image mc 5k = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/k.png")
image mc 5l = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/l.png")
image mc 5m = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/m.png")
image mc 5n = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/n.png")
image mc 5o = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/o.png")
image mc 5p = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/p.png")
image mc 5q = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/q.png")
image mc 5r = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/r.png")
image mc 5s = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/s.png")
image mc 5t = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/t.png")
image mc 5u = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/u.png")
image mc 5v = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/v.png")
image mc 5w = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/w.png")
image mc 5x = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/x.png")
image mc 5y = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/y.png")
image mc 5z = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/z.png")
image mc 5error = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/error.png")
image mc 5error1 = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/error1.png")
image mc 5shock = im.Composite((960, 960), (0, 0), "mod_assets/shared_assets/mc/3.png", (0, 0), "mod_assets/shared_assets/mc/shock.png")

#image mc_glitch: #MC GLITCH SPRITE ***UNUSED***
#    choice:
#        "mod_assets/shared_assets/mc/old/1.png"
#    choice:
#        "mod_assets/shared_assets/mc/old/2.png"
#    choice:
#        "mod_assets/shared_assets/mc/old/3.png"
#    choice:
#        "mod_assets/shared_assets/mc/old/4.png"
#    choice:
#        "mod_assets/shared_assets/mc/old/5.png"
#    0.15
#    repeat
