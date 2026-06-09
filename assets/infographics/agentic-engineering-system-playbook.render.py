# Agentic Engineering System — LinkedIn portrait infographic (1080x1350)
# Render pipeline:
#   python3 agentic-engineering-system-playbook.render.py
#   rsvg-convert -w 1080 -h 1350 agentic-engineering-system-playbook.svg -o agentic-engineering-system-playbook.png
# Fonts: Playfair Display (display), Helvetica Neue (body), Menlo (mono).
import math
CREAM="#F9F7F5"; INK="#1A1A1A"; LIME="#DAF172"; OLIVE="#5C6B1A"
CHARCO="#26261F"; BURNT="#C26B3F"; CARD="#FFFFFF"
W,H=1080,1350
HEAD="Playfair Display"; BODY="Helvetica Neue, Helvetica, Arial, sans-serif"; MONO="Menlo, monospace"
svg=[]; add=svg.append
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
add(f'<rect width="{W}" height="{H}" fill="{CREAM}"/>')
add(f'<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="6.5" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="{OLIVE}"/></marker></defs>')

M=56  # margin

# ===== HEADLINE BLOCK =====
add(f'<text x="{M}" y="74" font-family="{BODY}" font-size="20" font-weight="700" letter-spacing="4" fill="{OLIVE}">THE AGENTIC WORKFLOW PLAYBOOK</text>')
add(f'<text x="{M}" y="146" font-family="{HEAD}" font-size="60" font-weight="900" fill="{OLIVE}">loop engineering</text>')
add(f'<text x="{M}" y="210" font-family="{HEAD}" font-size="60" font-weight="900" fill="{INK}">is the biggest lever</text>')
add(f'<text x="{M}" y="274" font-family="{HEAD}" font-size="60" font-weight="900" fill="{INK}">on your<tspan dx="16" fill="{BURNT}">AI coding bill.</tspan></text>')
add(f'<text x="{M}" y="318" font-family="{BODY}" font-size="25" font-weight="600" fill="{INK}">Explore once, at frontier cost. Then reuse the workflow that pays back.</text>')
add(f'<line x1="{M}" y1="342" x2="{W-M}" y2="342" stroke="{OLIVE}" stroke-width="3"/>')

# ===== LEGEND (slim inline key) =====
ly=372
add(f'<rect x="{M}" y="{ly}" width="18" height="18" rx="3" fill="{BURNT}"/>')
add(f'<text x="{M+26}" y="{ly+15}" font-family="{BODY}" font-size="16" font-weight="700" fill="{INK}">SPEND TO LEARN</text>')
add(f'<line x1="300" y1="{ly-1}" x2="300" y2="{ly+19}" stroke="{OLIVE}" stroke-width="1" opacity="0.4"/>')
add(f'<rect x="320" y="{ly}" width="18" height="18" rx="3" fill="{LIME}" stroke="{OLIVE}" stroke-width="1.5"/>')
add(f'<text x="346" y="{ly+15}" font-family="{BODY}" font-size="16" font-weight="700" fill="{INK}">SPEND THAT PAYS BACK</text>')

# ===== LOOP =====
cx,cy,Rx,Ry=540,632,392,140
NW,NH=270,80
nodes=[("1","EXPLORE","frontier \u00b7 capped $",-90,True),
("2","CODIFY","persist as a reusable skill",-30,False),
("3","PUBLISH","portal skill, policy-gated",30,False),
("4","CONSUME","pull by manifest",90,False),
("5","RUN & MONITOR","cost-per-outcome",150,False),
("6","DISCOVER","usage reveals next",210,False)]
pos={}
for num,t,s,ang,exp in nodes:
    a=math.radians(ang); pos[num]=(cx+Rx*math.cos(a),cy+Ry*math.sin(a))
# center label
add(f'<text x="{cx}" y="{cy-34}" text-anchor="middle" font-family="{HEAD}" font-size="30" font-weight="900" fill="{OLIVE}">The Agentic Workflow</text>')
add(f'<text x="{cx}" y="{cy+2}" text-anchor="middle" font-family="{HEAD}" font-size="30" font-weight="900" fill="{OLIVE}">Lifecycle</text>')
add(f'<text x="{cx}" y="{cy+34}" text-anchor="middle" font-family="{BODY}" font-size="15" font-style="italic" fill="{INK}">one exploration becomes a</text>')
add(f'<text x="{cx}" y="{cy+54}" text-anchor="middle" font-family="{BODY}" font-size="15" font-style="italic" fill="{INK}">reusable, governed workflow</text>')

order=["1","2","3","4","5","6","1"]
def short(ax,ay,bx,by,d):
    l=math.hypot(bx-ax,by-ay) or 1; return ax+(bx-ax)/l*d,ay+(by-ay)/l*d
for i in range(6):
    x1,y1=pos[order[i]]; x2,y2=pos[order[i+1]]
    mx,my=(x1+x2)/2,(y1+y2)/2; dx,dy=mx-cx,my-cy; dl=math.hypot(dx,dy) or 1
    ctx,cty=mx+dx/dl*46,my+dy/dl*46
    dd=min(98, math.hypot(x2-x1,y2-y1)*0.36)
    sx,sy_=short(x1,y1,ctx,cty,dd); ex,ey=short(x2,y2,ctx,cty,dd)
    add(f'<path d="M{sx:.0f},{sy_:.0f} Q{ctx:.0f},{cty:.0f} {ex:.0f},{ey:.0f}" fill="none" stroke="{OLIVE}" stroke-width="3" marker-end="url(#arrow)" opacity="0.9"/>')
for num,title,sub,ang,exp in nodes:
    nx,ny=pos[num]; x=nx-NW/2; y=ny-NH/2
    if exp:
        add(f'<rect x="{x:.0f}" y="{y:.0f}" width="{NW}" height="{NH}" rx="12" fill="{CHARCO}" stroke="{BURNT}" stroke-width="3"/>')
        tcol=CREAM; scol=CREAM
    else:
        add(f'<rect x="{x:.0f}" y="{y:.0f}" width="{NW}" height="{NH}" rx="12" fill="{CARD}" stroke="{OLIVE}" stroke-width="2.5"/>')
        tcol=INK; scol=OLIVE
    add(f'<text x="{x+22:.0f}" y="{y+37:.0f}" font-family="{HEAD}" font-size="22" font-weight="800" fill="{tcol}">{title}</text>')
    add(f'<text x="{x+22:.0f}" y="{y+63:.0f}" font-family="{BODY}" font-size="16.5" fill="{scol}">{sub}</text>')

# ===== PORTFOLIO: EXAMPLE WORKFLOWS =====
add(f'<text x="{cx}" y="852" text-anchor="middle" font-family="{HEAD}" font-size="23" font-weight="900" fill="{OLIVE}"><tspan font-family="{BODY}" font-size="18" font-weight="700" fill="{INK}">Starter agentic workflows</tspan><tspan dx="10" font-family="{BODY}" font-size="18" font-weight="600" font-style="italic" fill="{INK}">\u2192 build your</tspan><tspan dx="12">Agentic Engineering System</tspan></text>')
chips=["code migration","code review","test generation","security upgrades","bug fixing"]
cap=''
for i,lab in enumerate(chips):
    if i>0:
        cap+=f'<tspan dx="7" fill="{OLIVE}" opacity="0.5">\u00b7</tspan><tspan dx="7">{lab}</tspan>'
    else:
        cap+=f'<tspan>{lab}</tspan>'
add(f'<text x="{cx}" y="892" text-anchor="middle" font-family="{MONO}" font-size="15.5" fill="{OLIVE}" letter-spacing="0.5">{cap}</text>')

# ===== MONEY: COST POOLS =====
PY=952
add(f'<text x="{M}" y="{PY}" font-family="{BODY}" font-size="16" font-weight="700" letter-spacing="3" fill="{OLIVE}">MONEY \u2014 COST POOLS</text>')
pools=[("Frontier R&D","capped \u00b7 best models","for AI frontier team"),
("Per-workflow run","metered by outcome","for approved use cases"),
("Everyday prompting","capped to cheaper models","the floor"),
("Local models","unmetered \u00b7 owned GPUs","free at margin")]
gap=18; pw=(W-2*M-3*gap)/4; ph=112; pyy=PY+22
# one ledger panel split into 4 pools (legend-coded accent bars)
colw=(W-2*M)/4
add(f'<rect x="{M}" y="{pyy}" width="{W-2*M}" height="{ph}" rx="12" fill="{CHARCO}"/>')
for k in (1,2,3):
    dvx=M+colw*k
    add(f'<line x1="{dvx:.0f}" y1="{pyy+16}" x2="{dvx:.0f}" y2="{pyy+ph-10}" stroke="{CREAM}" stroke-width="1" opacity="0.16"/>')
for i,(name,desc,tag) in enumerate(pools):
    px=M+i*colw+18
    acc=BURNT if i==0 else LIME
    add(f'<rect x="{px:.0f}" y="{pyy+14}" width="{colw-36:.0f}" height="4" rx="2" fill="{acc}"/>')
    add(f'<text x="{px:.0f}" y="{pyy+46}" font-family="{HEAD}" font-size="19" font-weight="800" fill="{CREAM}">{name}</text>')
    add(f'<text x="{px:.0f}" y="{pyy+72}" font-family="{BODY}" font-size="15" fill="{CREAM}">{desc}</text>')
    add(f'<text x="{px:.0f}" y="{pyy+96}" font-family="{MONO}" font-size="14" fill="{CREAM}" opacity="0.62">{tag}</text>')

# ===== MACHINERY: TECHNICAL PLAYBOOK =====
BY=1110
BX,BW,BH=M,W-2*M,160
add(f'<rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="14" fill="{CARD}" stroke="{OLIVE}" stroke-width="2.5"/>')
add(f'<text x="{BX+26}" y="{BY+42}" font-family="{HEAD}" font-size="24" font-weight="800" fill="{INK}">TOOLING \u2014 The Technical Playbook</text>')
add(f'<line x1="{BX+26}" y1="{BY+56}" x2="{BX+BW-26}" y2="{BY+56}" stroke="{OLIVE}" stroke-width="1" opacity="0.4"/>')
steps=[("1","PACKAGE","Agent Package Manager","bundles the workflow"),
("2","GOVERN","apm-policy.yaml gates","who runs it, which models."),
("3","DISTRIBUTE","A signed registry","hands it out, traceable."),
("4","CONSUME","Pull by manifest+lockfile;","policy re-checked on run.")]
colw=(BW-52)/4; sx0=BX+26; topy=BY+86
for i,(num,name,l1,l2) in enumerate(steps):
    cx0=sx0+i*colw
    add(f'<text x="{cx0:.0f}" y="{topy+2:.0f}" font-family="{HEAD}" font-size="20" font-weight="800" fill="{OLIVE}">{num}  {name}</text>')
    add(f'<text x="{cx0:.0f}" y="{topy+34:.0f}" font-family="{BODY}" font-size="16" fill="{INK}">{l1}</text>')
    add(f'<text x="{cx0:.0f}" y="{topy+56:.0f}" font-family="{BODY}" font-size="16" fill="{INK}">{l2}</text>')

# ===== FOOTER =====
add(f'<text x="{M}" y="1292" font-family="{BODY}" font-size="15" fill="{OLIVE}">A Center of Enablement funds the pools and maintains the lifecycle. Everyone else consumes proven workflows.</text>')
add('</svg>')
open("agentic-engineering-system-playbook.svg","w").write("\n".join(svg))
print("ok",len(svg))
