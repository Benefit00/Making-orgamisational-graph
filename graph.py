from graphviz import Digraph

# Create a directed graph
dot = Digraph(comment="Information Security Department Org Chart", format="png")
dot.attr(rankdir='TB', size='8')

# Top level - CISO
dot.node("CISO", "CISO\n[Chief Information Security Officer]", shape="box", style="filled", fillcolor="#cfe2f3")

# Domains
domains = {
    "compliance": "[compliance]",
    "ops": "[security operations]",
    "ops blue team": "[blue team]",
    "ops red team" : "[red team]", 
    "grc": "[governance, risk & compliance]"
}

# Heads
dot.node("HeadSec", "Head of Information Security [sec]", shape="box", fillcolor="#f4cccc", style="filled")
dot.node("HeadOps", "Head of Security Operations [ops]", shape="box", fillcolor="#f4cccc", style="filled")
dot.node("HeadGRC", "Head of GRC [grc]", shape="box", fillcolor="#f4cccc", style="filled")

# Connect CISO to Heads
dot.edges([("CISO", "HeadSec"), ("CISO", "HeadOps"), ("CISO", "HeadGRC")])

# Security Engineering Managers
dot.node("SEMsec", "Security Engineering Manager [sem sec]", shape="box", fillcolor="#d9ead3", style="filled")
dot.node("SEMops", "Security Engineering Manager [sem ops]", shape="box", fillcolor="#d9ead3", style="filled")
dot.node("SEMblue", "Security Engineering Manager [sem blue]", shape="box", fillcolor="#d9ead3", style="filled")
dot.node("SEMgrc", "Security Engineering Manager [sem grc]", shape="box", fillcolor="#d9ead3", style="filled")

dot.edges([("HeadSec", "SEMsec"), ("HeadOps", "SEMops"), ("HeadBlue", "SEMblue"), ("HeadGRC", "SEMgrc")])

# Team Leads
dot.node("TLsec", "Team Lead [tl sec]", shape="box", fillcolor="#fff2cc", style="filled")
dot.node("TLops", "Team Lead [tl ops]", shape="box", fillcolor="#fff2cc", style="filled")
dot.node("TLblue", "Team Lead [tl blue]", shape="box", fillcolor="#fff2cc", style="filled")
dot.node("TLgrc", "Team Lead [tl grc]", shape="box", fillcolor="#fff2cc", style="filled")

dot.edges([("SEMsec", "TLsec"), ("SEMops", "TLops"), ("SEMblue", "TLblue"), ("SEMgrc", "TLgrc")])

# Individual Contributors
dot.node("SecEng", "Security Engineer", shape="ellipse", fillcolor="#e6e6e6", style="filled")
dot.node("SecSpec", "Security Specialist", shape="ellipse", fillcolor="#e6e6e6", style="filled")
dot.node("SecSpecBlue", "Security Specialist (Blue Team)", shape="ellipse", fillcolor="#e6e6e6", style="filled")
dot.node("GRCMgr", "GRC Manager", shape="ellipse", fillcolor="#e6e6e6", style="filled")
dot.node("GRCSpecialist", "GRC Specialist", shape="ellipse", fillcolor="#e6e6e6", style="filled")

dot.edges([("TLsec", "SecEng"), ("TLops", "SecSpec"), ("TLblue", "SecSpecBlue"), ("TLgrc", "GRCMgr"), ("GRCMgr", "GRCSpecialist")])

# Render the chart
output_path = '/mnt/data/infosec_org_chart'
dot.render(output_path, cleanup=True)

output_path + ".png"
