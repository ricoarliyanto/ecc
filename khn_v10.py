
import streamlit as st
import streamlit.components.v1 as components
import math, random, time, base64
from datetime import datetime

st.set_page_config(page_title="HOIP | Hydropower Operational Intelligence Platform", page_icon="🌊", layout="wide")

KHN_LOGO_B64 = "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"


if "tick" not in st.session_state:
    st.session_state.tick = 0
st.session_state.tick += 1
t = st.session_state.tick

def live(base, amp=1, freq=20, noise=0.1):
    return base + amp * math.sin(t / freq) + random.uniform(-noise, noise)

data = {
    "plant_health": live(97.4, .4, 40, .05),
    "dam_health": live(98.2, .25, 32, .04),
    "reservoir_level": live(326.42, .35, 36, .03),
    "reservoir_pct": live(82.5, 2.2, 42, .2),
    "generation": live(1188, 45, 27, 5),
    "energy_today": live(18.7, .6, 24, .05),
    "inflow": live(846, 70, 18, 12),
    "outflow": live(721, 54, 23, 8),
    "rainfall": max(0, live(12.4, 7.5, 21, 1.2)),
    "turbine_health": live(96.8, .6, 37, .08),
    "electrical_health": live(97.1, .5, 35, .08),
    "switchyard_health": live(98.7, .25, 39, .04),
    "maintenance_risk": live(13.2, 2.2, 29, .2),
    "co2_avoided": live(12840, 250, 50, 25),
    "freq": live(50.01, .04, 12, .01),
    "pf": live(.987, .006, 19, .002),
    "vib": live(2.1, .25, 14, .04),
    "bearing_temp": live(64.2, 1.8, 31, .15),
    "seepage": live(18.6, 1.4, 33, .2),
    "piezometer": live(142.3, 3.2, 28, .3),
    "wind_speed": live(3.8, 1.4, 17, .2),
    "ambient_temp": live(27.8, 1.6, 29, .1),
    "humidity": live(78, 6, 25, .7),
    "solar_rad": max(0, live(620, 180, 31, 15)),
    "pm25": max(2, live(18, 7, 19, 1.1)),
    "pm10": max(5, live(42, 11, 23, 1.8)),
    "co": max(.1, live(.42, .12, 21, .02)),
    "no2": max(1, live(14, 4, 26, .6)),
    "ph": live(7.18, .22, 22, .03),
    "turbidity": max(0, live(22, 8, 17, .8)),
    "do": live(7.4, .5, 24, .08),
    "conductivity": live(184, 18, 27, 2),
    "water_temp": live(25.4, .8, 30, .1),
    "corr_score": live(91.5, 2.2, 28, .2),
}

st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
html, body, [class*="css"] {font-family: Inter, sans-serif;}
#MainMenu, footer {visibility:hidden;}
[data-testid="stHeader"] {background:rgba(0,0,0,0); height:0rem;}
[data-testid="stToolbar"] {right:1.1rem; top:.45rem;}
.stApp {
  background:
    radial-gradient(circle at 14% 3%, rgba(52,211,153,.20), transparent 27%),
    radial-gradient(circle at 82% 6%, rgba(94,234,212,.13), transparent 26%),
    radial-gradient(circle at 54% 92%, rgba(45,212,191,.08), transparent 35%),
    linear-gradient(135deg,#02150f 0%,#06261d 35%,#071923 68%,#041018 100%);
  color:#eef7ff;
}
.block-container {padding-top:.55rem; max-width:1580px; padding-left:1.15rem; padding-right:1.15rem;}
[data-testid="stSidebar"] {
  background:
    radial-gradient(circle at 15% 8%, rgba(52,211,153,.16), transparent 30%),
    linear-gradient(180deg,rgba(3,42,31,.98),rgba(4,30,29,.98) 48%,rgba(3,15,22,.99));
  border-right:1px solid rgba(45,212,191,.28);
  box-shadow:18px 0 50px rgba(0,0,0,.24);
}
[data-testid="stSidebar"] * {color:#dffbf1;}
[data-testid="stSidebar"] [role="radiogroup"] label {
  border-radius:12px; padding:7px 9px; margin:2px 0; border:1px solid rgba(255,255,255,0);
}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {
  background:rgba(52,211,153,.08); border-color:rgba(52,211,153,.16);
}
[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"],
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
  background:linear-gradient(90deg,rgba(16,185,129,.48),rgba(13,148,136,.18));
  border-left:4px solid #5eead4;
  box-shadow:0 12px 28px rgba(16,185,129,.18);
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2{color:#5eead4; letter-spacing:-.4px;}
.hoip-topbar{
  display:flex; justify-content:space-between; align-items:center; gap:18px;
  padding:18px 22px; border:1px solid rgba(94,234,212,.24);
  background:
    linear-gradient(135deg,rgba(9,78,56,.78),rgba(5,45,39,.72) 45%,rgba(4,22,29,.70)),
    radial-gradient(circle at 22% 0%, rgba(52,211,153,.24), transparent 36%);
  border-radius:24px; box-shadow:0 18px 55px rgba(0,0,0,.34), inset 0 1px 0 rgba(255,255,255,.06);
  backdrop-filter:blur(18px); margin-bottom:18px; position:relative; overflow:hidden;
}
.hoip-topbar:before{content:"";position:absolute;left:-70px;top:-90px;width:330px;height:250px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.22),transparent 66%);pointer-events:none;}
.hoip-brand{display:flex;align-items:center;gap:18px;position:relative;z-index:1;}
.khn-logo{width:176px;max-height:70px;object-fit:contain;filter:drop-shadow(0 10px 22px rgba(0,0,0,.35));}
.brand-divider{width:1px;height:58px;background:linear-gradient(180deg,transparent,rgba(94,234,212,.55),transparent);}
.brand-title{font-size:27px; font-weight:900; letter-spacing:-.8px; line-height:1; color:#f2fff9;}
.brand-subtitle{color:#b6e7db; font-size:13px; margin-top:8px;}
.status-pill{padding:10px 14px; border-radius:999px; border:1px solid rgba(52,211,153,.42); background:rgba(16,185,129,.12); color:#b8ffd6; font-weight:800; font-size:13px; display:inline-flex; gap:8px; align-items:center; box-shadow:inset 0 1px 0 rgba(255,255,255,.05);}
.pulse{width:8px;height:8px;border-radius:50%;background:#67e8a5;box-shadow:0 0 0 0 rgba(103,232,165,.65);animation:pulse 2.4s infinite;}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(103,232,165,.60)}70%{box-shadow:0 0 0 9px rgba(103,232,165,0)}100%{box-shadow:0 0 0 0 rgba(103,232,165,0)}}
.kpi-card{
  border:1px solid rgba(94,234,212,.20);
  background:linear-gradient(160deg,rgba(7,57,45,.76),rgba(4,24,30,.66));
  border-radius:22px; padding:18px; min-height:122px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.04),0 18px 42px rgba(0,0,0,.22);
  position:relative; overflow:hidden;
}
.kpi-card:before{content:""; position:absolute; right:-28px; top:-30px; width:100px;height:100px;border-radius:50%; background:radial-gradient(circle,rgba(52,211,153,.22),transparent 68%);}
.kpi-label{color:#a7cfc4;font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.8px;}
.kpi-value{font-size:31px;font-weight:900;margin-top:10px;letter-spacing:-.8px;}
.kpi-unit{font-size:17px;color:#a7cfc4;margin-left:4px;}
.kpi-note{color:#b4d8cf;font-size:12px;margin-top:8px;}
.panel{
  border:1px solid rgba(94,234,212,.20);
  background:linear-gradient(160deg,rgba(7,54,45,.72),rgba(3,22,28,.68));
  border-radius:26px; padding:18px; box-shadow:0 22px 60px rgba(0,0,0,.24); backdrop-filter:blur(14px);
}
.panel-title{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;}
.panel-title h3{margin:0;font-size:18px;letter-spacing:-.2px;}
.panel-title span{color:#a7cfc4;font-size:12px;}
.ai-box{border:1px solid rgba(94,234,212,.24);background:linear-gradient(145deg,rgba(52,211,153,.12),rgba(8,21,38,.42));border-radius:22px;padding:16px;margin-bottom:12px;}
.ai-title{font-size:13px;color:#7fffd4;font-weight:900;text-transform:uppercase;letter-spacing:.8px;}
.ai-text{font-size:14px;color:#e8f7ff;line-height:1.55;margin-top:8px;}
.metric-row{display:grid;grid-template-columns:1fr auto;gap:8px;border-bottom:1px solid rgba(94,234,212,.10);padding:10px 0;}
.metric-row:last-child{border-bottom:0;}
.metric-name{color:#c7d9e9;font-size:13px;}
.metric-value{font-size:13px;font-weight:900;color:#fff;}
.asset-chip{display:inline-flex;align-items:center;gap:8px;padding:8px 11px;border-radius:999px;border:1px solid rgba(94,234,212,.18);background:rgba(255,255,255,.045);font-size:12px;color:#d4fff2;margin:4px 5px 4px 0;}
.dot-green{width:7px;height:7px;border-radius:50%;background:#67e8a5;}
.dot-amber{width:7px;height:7px;border-radius:50%;background:#ffd166;}

.footer-note{color:rgba(220,240,255,.54);font-size:11px;text-align:center;margin-top:18px;}
.module-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:12px;}
.module-card{border:1px solid rgba(94,234,212,.16);background:linear-gradient(160deg,rgba(8,52,43,.72),rgba(3,23,29,.60));border-radius:20px;padding:16px;min-height:150px;position:relative;overflow:hidden;}
.module-card:before{content:"";position:absolute;right:-25px;top:-25px;width:80px;height:80px;border-radius:50%;background:radial-gradient(circle,rgba(52,211,153,.16),transparent 70%);}
.module-title{font-size:15px;font-weight:900;color:#eef8ff;margin-bottom:8px;}
.module-text{font-size:12px;line-height:1.5;color:#aac4da;}
.tag{display:inline-flex;padding:5px 8px;border-radius:999px;border:1px solid rgba(103,232,165,.28);color:#b8ffd6;background:rgba(103,232,165,.08);font-size:10px;font-weight:900;margin-top:10px;}
.timeline{position:relative;padding-left:18px;border-left:2px solid rgba(56,213,255,.24);}
.timeline-item{margin:0 0 16px 0;padding:12px 14px;border-radius:18px;background:rgba(255,255,255,.045);border:1px solid rgba(94,234,212,.13);}
.timeline-item b{color:#eef8ff}.timeline-item p{margin:6px 0 0;color:#a9bfd3;font-size:12px;line-height:1.45;}
.value-number{font-size:42px;font-weight:900;letter-spacing:-1.4px;color:#eef8ff;line-height:1}.value-caption{font-size:12px;color:#a7cfc4;margin-top:8px;line-height:1.45;}
.station-card{border:1px solid rgba(94,234,212,.17);background:linear-gradient(155deg,rgba(8,54,45,.78),rgba(3,22,28,.66));border-radius:22px;padding:16px;min-height:178px;position:relative;overflow:hidden;margin-bottom:12px}.station-card:after{content:"";position:absolute;right:-34px;bottom:-34px;width:110px;height:110px;border-radius:50%;background:radial-gradient(circle,rgba(52,211,153,.14),transparent 70%)}.station-icon{font-size:24px;margin-bottom:8px}.station-name{font-size:16px;font-weight:900;color:#eef8ff}.station-meta{font-size:11px;color:#a7cfc4;margin:5px 0 11px}.station-param{display:flex;justify-content:space-between;border-top:1px solid rgba(94,234,212,.09);padding-top:8px;margin-top:8px;font-size:12px}.station-param span{color:#a9bfd3}.station-param b{color:#fff}.risk-chip{display:inline-flex;padding:6px 9px;border-radius:999px;background:rgba(103,232,165,.10);border:1px solid rgba(103,232,165,.28);color:#b8ffd6;font-size:10px;font-weight:900}.corr-line{padding:12px 14px;margin:10px 0;border-radius:18px;background:rgba(255,255,255,.045);border:1px solid rgba(94,234,212,.13)}.corr-line b{color:#eef8ff}.corr-line p{margin:6px 0 0;color:#a9bfd3;font-size:12px;line-height:1.45}

/* Elite micro-animations */
.station-card.weather-rain{isolation:isolate;}
.station-card.weather-rain .rain-layer{position:absolute;inset:0;border-radius:22px;overflow:hidden;pointer-events:none;z-index:0;opacity:.9;}
.station-card.weather-rain .rain-layer:before,
.station-card.weather-rain .rain-layer:after{content:"";position:absolute;inset:-40px 0;background-repeat:repeat;background-size:110px 120px;filter:drop-shadow(0 0 6px rgba(125,245,255,.35));}
.station-card.weather-rain .rain-layer:before{background-image:linear-gradient(115deg,transparent 0 43%,rgba(129,231,255,.85) 44% 46%,transparent 47% 100%);animation:rainFallA .85s linear infinite;opacity:.38;}
.station-card.weather-rain .rain-layer:after{background-image:linear-gradient(115deg,transparent 0 50%,rgba(94,234,212,.72) 51% 53%,transparent 54% 100%);background-size:160px 160px;animation:rainFallB 1.25s linear infinite;opacity:.28;}
.station-card.weather-rain > *:not(.rain-layer){position:relative;z-index:2;}
.station-card.weather-rain:before{content:"";position:absolute;left:18px;right:18px;bottom:10px;height:36px;background:radial-gradient(ellipse at center,rgba(94,234,212,.18),transparent 70%);z-index:1;animation:wetGlow 2.2s ease-in-out infinite;}
@keyframes rainFallA{from{transform:translate3d(-25px,-70px,0)}to{transform:translate3d(35px,70px,0)}}
@keyframes rainFallB{from{transform:translate3d(20px,-100px,0)}to{transform:translate3d(-30px,80px,0)}}
@keyframes wetGlow{0%,100%{opacity:.35}50%{opacity:.75}}
.live-spark{height:2px;width:100%;margin-top:12px;border-radius:99px;background:linear-gradient(90deg,rgba(94,234,212,.08),rgba(94,234,212,.78),rgba(52,211,153,.08));background-size:220% 100%;animation:sparkDrift 2s linear infinite;}
.svg-live-num{fill:#ffffff;font-weight:900;filter:drop-shadow(0 0 8px rgba(94,234,212,.45));}
.unit-live{filter:drop-shadow(0 0 12px rgba(103,232,165,.9));animation:unitPulse 1.35s ease-in-out infinite;}
@keyframes unitPulse{0%,100%{opacity:.58}50%{opacity:1}}
@keyframes sparkDrift{from{background-position:0% 0}to{background-position:220% 0}}

/* Touchdown premium live layer */
.kpi-card{animation:cardBreath 5.8s ease-in-out infinite;}
.kpi-card:nth-child(2n){animation-delay:.8s}.kpi-card:nth-child(3n){animation-delay:1.6s}
@keyframes cardBreath{0%,100%{box-shadow:inset 0 1px 0 rgba(255,255,255,.04),0 18px 42px rgba(0,0,0,.22),0 0 0 rgba(94,234,212,0)}50%{box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 24px 58px rgba(0,0,0,.28),0 0 28px rgba(94,234,212,.14)}}
.kpi-icon,.metric-icon{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;margin-right:8px;border-radius:9px;background:rgba(94,234,212,.10);border:1px solid rgba(94,234,212,.20);color:#7fffd4;font-weight:900;box-shadow:0 0 12px rgba(94,234,212,.10)}
.metric-icon{width:18px;height:18px;font-size:11px;border-radius:7px;margin-right:6px;vertical-align:middle}
.live-updated{margin-top:7px;color:#82bbae;font-size:10.5px;letter-spacing:.02em;opacity:.82}
.ai-insight-banner{position:relative;margin:0 0 14px 0;border-radius:18px;overflow:hidden;border:1px solid rgba(94,234,212,.24);background:linear-gradient(90deg,rgba(9,78,56,.70),rgba(4,27,36,.82));box-shadow:0 16px 42px rgba(0,0,0,.22),0 0 24px rgba(94,234,212,.08)}
.ai-insight-track{display:flex;width:max-content;animation:insightScroll 56s linear infinite;white-space:nowrap}
.ai-insight{padding:12px 32px 12px 18px;color:#eafff9;font-size:13.2px;font-weight:800;letter-spacing:.01em}.ai-insight b{color:#7fffd4}.ai-insight.amber b{color:#ffd166}.ai-insight:before{content:'●';color:#67e8a5;margin-right:8px;text-shadow:0 0 12px rgba(103,232,165,.9)}.ai-insight.amber:before{color:#ffd166;text-shadow:0 0 12px rgba(255,209,102,.9)}
@keyframes insightScroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.ai-insight-banner:after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(3,18,24,.95),transparent 8%,transparent 92%,rgba(3,18,24,.95));pointer-events:none}



/* Subsystem Command Centre v3 - robust HTML/CSS map */
.subsystem-map-panel{height:610px;padding:0!important;overflow:hidden;position:relative;background:linear-gradient(160deg,rgba(4,38,33,.78),rgba(3,16,26,.72));}
.subsystem-map-panel:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 18% 18%,rgba(94,234,212,.10),transparent 28%),radial-gradient(circle at 72% 55%,rgba(255,209,102,.07),transparent 30%),repeating-linear-gradient(45deg,rgba(94,234,212,.045) 0 1px,transparent 1px 58px),repeating-linear-gradient(-45deg,rgba(94,234,212,.035) 0 1px,transparent 1px 58px);}
.subsystem-map-panel:after{content:"";position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(160deg,transparent,rgba(7,49,40,.35));clip-path:polygon(0 70%,20% 58%,43% 64%,60% 48%,78% 66%,100% 42%,100% 100%,0 100%);}
.subsys-title{position:absolute;left:38px;top:32px;font-size:24px;font-weight:900;color:#f2fff9;letter-spacing:-.4px;z-index:3;}
.subsys-subtitle{position:absolute;left:38px;top:68px;font-size:12px;color:#a7cfc4;z-index:3;max-width:850px;}
.subsys-stage{position:absolute;left:0;right:0;top:0;bottom:0;z-index:2;}
.node{position:absolute;width:118px;height:118px;border-radius:50%;background:radial-gradient(circle at 42% 26%,#154b69 0%,#0a253d 58%,#071726 100%);border:1px solid rgba(94,234,212,.38);box-shadow:0 20px 45px rgba(0,0,0,.35),0 0 22px rgba(94,234,212,.16);display:flex;align-items:center;justify-content:center;animation:nodeFloat 3.1s ease-in-out infinite;}
.node b{font-size:11px;font-weight:900;color:#b8ffd6;text-shadow:0 0 10px rgba(184,255,214,.75);letter-spacing:.6px;}
.node em{position:absolute;left:50%;top:54%;width:16px;height:16px;margin-left:-8px;margin-top:-8px;border-radius:50%;background:#67e8a5;box-shadow:0 0 18px rgba(103,232,165,.92);}
.dam-core{width:158px;height:158px;background:radial-gradient(circle at 44% 30%,#5a411a 0%,#12354a 56%,#061523 100%);border:2px solid rgba(255,209,102,.55);box-shadow:0 22px 62px rgba(0,0,0,.42),0 0 34px rgba(255,209,102,.18);animation:damPulse 2.5s ease-in-out infinite;}
.dam-core i{position:absolute;inset:-18px;border:2px solid rgba(255,209,102,.32);border-radius:50%;animation:radarRing 2.8s ease-out infinite;}
.dam-core b{color:#ffd166;font-size:12px;}
.dam-core em{background:#ffd166;box-shadow:0 0 18px rgba(255,209,102,.95);}
.node-label{position:absolute;min-width:124px;padding:8px 11px;border-radius:13px;background:rgba(2,18,26,.78);border:1px solid rgba(94,234,212,.22);box-shadow:0 12px 22px rgba(0,0,0,.35);text-align:center;backdrop-filter:blur(8px);}
.node-label strong{display:block;color:#eef8ff;font-size:13px;font-weight:900;line-height:1.1}.node-label small{display:block;color:#b6d8d0;font-size:11px;margin-top:5px;white-space:nowrap;}
.n-weather{left:95px;top:116px}.lab-weather{left:92px;top:242px}.n-env{left:405px;top:118px;animation-delay:.25s}.lab-env{left:403px;top:244px}.n-res{left:730px;top:138px;animation-delay:.5s}.lab-res{left:725px;top:270px}.n-wq{left:113px;top:354px;animation-delay:.7s}.lab-wq{left:93px;top:480px}.dam-core{left:390px;top:342px}.lab-dam{left:405px;top:512px}.n-turb{left:725px;top:365px;animation-delay:.85s}.lab-turb{left:718px;top:492px}.n-grid{left:900px;top:148px;animation-delay:1s}.lab-grid{left:884px;top:280px}
.flow-line{position:absolute;height:4px;border-radius:99px;background:linear-gradient(90deg,rgba(94,234,212,.12),rgba(125,249,255,.88),rgba(103,232,165,.88),rgba(255,209,102,.20));box-shadow:0 0 16px rgba(94,234,212,.34);overflow:hidden;transform-origin:left center;}
.flow-line:before{content:"";position:absolute;inset:1px;background:repeating-linear-gradient(90deg,transparent 0 18px,rgba(255,255,255,.75) 18px 31px,transparent 31px 48px);animation:flowDash 1.6s linear infinite;}
.flow-line span{position:absolute;top:50%;left:-10px;width:10px;height:10px;margin-top:-5px;border-radius:50%;background:#7df9ff;box-shadow:0 0 14px rgba(125,249,255,.95);animation:packetMove 2.4s linear infinite;}
.flow-line.muted{opacity:.55}.flow-line.muted span{background:#ffd166;}
.l-weather-res{left:210px;top:175px;width:215px;transform:rotate(-7deg)}.l-env-res{left:520px;top:176px;width:225px;transform:rotate(5deg)}.l-res-dam{left:615px;top:302px;width:226px;transform:rotate(132deg)}.l-dam-turb{left:542px;top:435px;width:196px;transform:rotate(3deg)}.l-turb-grid{left:825px;top:365px;width:154px;transform:rotate(-51deg)}.l-wq-dam{left:230px;top:438px;width:173px;transform:rotate(10deg)}
.active-path-card,.corr-card-mini{position:absolute;border-radius:18px;background:rgba(8,55,45,.84);border:1px solid rgba(103,232,165,.24);box-shadow:0 15px 35px rgba(0,0,0,.25);padding:13px 16px;backdrop-filter:blur(8px)}
.active-path-card{left:34px;bottom:30px;width:360px}.active-path-card b,.corr-card-mini b{display:block;color:#8fffe0;font-size:11px;font-weight:900;letter-spacing:1px}.active-path-card span{display:block;color:#eef8ff;font-size:13px;font-weight:800;margin-top:7px}.corr-card-mini{right:36px;bottom:30px;width:230px}.corr-card-mini strong{display:inline-block;color:#eef8ff;font-size:28px;font-weight:900;margin-top:7px;margin-right:10px}.corr-card-mini span{font-size:12px;font-weight:900;letter-spacing:.8px}
@keyframes nodeFloat{0%,100%{transform:translateY(0);filter:drop-shadow(0 0 4px rgba(94,234,212,.20))}50%{transform:translateY(-4px);filter:drop-shadow(0 0 15px rgba(94,234,212,.65))}}
@keyframes damPulse{0%,100%{filter:drop-shadow(0 0 7px rgba(255,209,102,.45))}50%{filter:drop-shadow(0 0 24px rgba(255,209,102,.95))}}
@keyframes radarRing{0%{transform:scale(.88);opacity:.55}100%{transform:scale(1.35);opacity:0}}
@keyframes flowDash{to{transform:translateX(48px)}}
@keyframes packetMove{from{left:-12px}to{left:100%}}


/* Subsystem Coverage Map v2 */
.coverage-hero{display:flex;justify-content:space-between;align-items:flex-start;gap:22px;padding:24px 28px;margin-bottom:18px;border:1px solid rgba(94,234,212,.18);border-radius:28px;background:linear-gradient(145deg,rgba(7,54,45,.78),rgba(3,22,28,.60));position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.22)}
.coverage-hero:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 18% 12%,rgba(94,234,212,.20),transparent 28%),radial-gradient(circle at 82% 20%,rgba(255,209,102,.12),transparent 24%),repeating-linear-gradient(45deg,rgba(94,234,212,.035) 0 1px,transparent 1px 48px);pointer-events:none}.coverage-hero>*{position:relative;z-index:1}.coverage-eyebrow{font-size:12px;font-weight:900;letter-spacing:1.4px;color:#7fffd4}.coverage-title{font-size:28px;font-weight:900;letter-spacing:-.7px;color:#f2fff9;margin-top:6px}.coverage-subtitle{font-size:13px;color:#b6d8d0;margin-top:8px;max-width:820px}.coverage-legend{display:grid;grid-template-columns:1fr 1fr;gap:8px;min-width:380px}.coverage-legend span{font-size:11px;font-weight:900;color:#d8fff3;border:1px solid rgba(94,234,212,.15);background:rgba(255,255,255,.045);border-radius:999px;padding:8px 10px}.lg{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:7px}.lg.auto{background:#67e8a5}.lg.op{background:#5eead4}.lg.lab{background:#ffd166}.lg.manual{background:#f59e0b}.coverage-map-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.coverage-card{min-height:300px;border:1px solid rgba(94,234,212,.18);border-radius:24px;padding:18px;background:linear-gradient(160deg,rgba(7,54,45,.76),rgba(3,22,28,.66));box-shadow:0 22px 52px rgba(0,0,0,.22);position:relative;overflow:hidden;transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease}.coverage-card:before{content:"";position:absolute;right:-38px;top:-42px;width:135px;height:135px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.18),transparent 70%)}.coverage-card:after{content:"";position:absolute;left:0;right:0;bottom:0;height:70px;background:linear-gradient(90deg,rgba(94,234,212,.03),rgba(94,234,212,.13),rgba(255,209,102,.05));transform:translateX(-55%);animation:coverageSweep 4.5s linear infinite}.coverage-card:hover{transform:translateY(-4px);border-color:rgba(126,255,212,.48);box-shadow:0 28px 70px rgba(0,0,0,.28),0 0 30px rgba(94,234,212,.12)}.coverage-card-top{display:flex;justify-content:space-between;align-items:center;position:relative;z-index:1}.cov-icon{width:48px;height:48px;border-radius:18px;background:rgba(255,255,255,.055);border:1px solid rgba(94,234,212,.18);display:flex;align-items:center;justify-content:center;font-size:24px}.cov-ring{--p:90;width:62px;height:62px;border-radius:50%;display:grid;place-items:center;background:conic-gradient(#67e8a5 calc(var(--p)*1%),rgba(255,255,255,.07) 0);box-shadow:0 0 18px rgba(103,232,165,.16)}.coverage-card.lab .cov-ring{background:conic-gradient(#ffd166 calc(var(--p)*1%),rgba(255,255,255,.07) 0)}.coverage-card.manual .cov-ring{background:conic-gradient(#f59e0b calc(var(--p)*1%),rgba(255,255,255,.07) 0)}.cov-ring span{width:49px;height:49px;border-radius:50%;display:grid;place-items:center;background:#06231e;font-size:13px;font-weight:900;color:#f2fff9}.cov-title{position:relative;z-index:1;margin-top:14px;color:#f2fff9;font-size:17px;font-weight:900;letter-spacing:-.2px}.cov-body{position:relative;z-index:1;margin-top:8px;color:#b9d3cc;font-size:12px;line-height:1.55;min-height:57px}.cov-meta{position:relative;z-index:1;display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:14px}.cov-meta div{border:1px solid rgba(94,234,212,.12);background:rgba(255,255,255,.035);border-radius:14px;padding:9px 8px}.cov-meta small{display:block;color:#8fbdb3;font-size:9px;font-weight:900;text-transform:uppercase;letter-spacing:.55px}.cov-meta strong{display:block;color:#eef8ff;font-size:11px;margin-top:4px;line-height:1.2}.cov-chips{position:relative;z-index:1;display:flex;flex-wrap:wrap;gap:6px;margin-top:13px}.cov-chips span{font-size:10px;font-weight:800;color:#b8ffd6;background:rgba(103,232,165,.08);border:1px solid rgba(103,232,165,.18);border-radius:999px;padding:5px 8px}.cov-footer{position:relative;z-index:1;display:flex;justify-content:space-between;align-items:flex-end;gap:12px;margin-top:14px}.cov-badge{font-size:10px;font-weight:900;border-radius:999px;padding:7px 10px;border:1px solid rgba(103,232,165,.25);color:#b8ffd6;background:rgba(103,232,165,.09)}.cov-badge.op{border-color:rgba(94,234,212,.28);color:#d8fffb;background:rgba(94,234,212,.08)}.cov-badge.lab{border-color:rgba(255,209,102,.33);color:#ffe3a3;background:rgba(255,209,102,.08)}.cov-badge.manual{border-color:rgba(245,158,11,.34);color:#ffd59a;background:rgba(245,158,11,.08)}.mini-spark{height:42px;display:flex;align-items:flex-end;gap:3px;opacity:.9}.mini-spark b{display:block;width:5px;border-radius:999px;background:linear-gradient(180deg,#5eead4,#67e8a5);animation:sparkBounce 2.4s ease-in-out infinite}.coverage-card.lab .mini-spark b{background:linear-gradient(180deg,#ffd166,#5eead4)}.coverage-card.manual .mini-spark b{background:linear-gradient(180deg,#f59e0b,#ffd166)}.mini-spark b:nth-child(2n){animation-delay:.18s}.mini-spark b:nth-child(3n){animation-delay:.34s}.coverage-summary-bar{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-top:16px;border:1px solid rgba(94,234,212,.18);border-radius:22px;padding:12px;background:rgba(3,23,29,.55)}.coverage-summary-bar div{border-radius:16px;background:rgba(255,255,255,.035);padding:12px 14px}.coverage-summary-bar span{display:block;color:#a7cfc4;font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.8px}.coverage-summary-bar b{display:block;margin-top:5px;color:#f2fff9;font-size:20px}@keyframes coverageSweep{from{transform:translateX(-75%)}to{transform:translateX(130%)}}@keyframes sparkBounce{0%,100%{opacity:.45;transform:scaleY(.82)}50%{opacity:1;transform:scaleY(1.08)}}


.kpi-icon{display:inline-grid;place-items:center;width:24px;height:24px;margin-right:9px;border-radius:9px;border:1px solid rgba(94,234,212,.22);background:rgba(94,234,212,.08);color:#7fffd4;font-size:14px;vertical-align:middle;box-shadow:0 0 14px rgba(94,234,212,.10)}
.metric-icon{display:inline-grid;place-items:center;width:20px;height:20px;margin-right:7px;border-radius:7px;border:1px solid rgba(94,234,212,.18);background:rgba(94,234,212,.06);color:#7fffd4;font-size:11px;vertical-align:middle}.hoip-live-number{transition:all .28s ease;text-shadow:0 0 12px rgba(94,234,212,.18)}
[data-testid="stSidebar"] [role="radiogroup"] label p{display:flex;align-items:center;gap:9px;}


/* Executive Command Center fix */
.filled-panel{min-height:390px;animation:panelBreath 5.8s ease-in-out infinite;}
.exec-panel .panel-title{margin-bottom:14px;}
.mini-summary-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:12px;}
.mini-summary{border:1px solid rgba(94,234,212,.18);background:rgba(255,255,255,.045);border-radius:16px;padding:11px;text-align:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.04)}
.mini-summary .mini-icon{font-size:20px;margin-bottom:4px}.mini-summary b{display:block;font-size:19px;color:#f2fff9}.mini-summary span{font-size:10px;color:#a7cfc4;text-transform:uppercase;font-weight:800;letter-spacing:.4px}
.health-list{display:grid;gap:9px}.health-row{display:grid;grid-template-columns:1fr auto;gap:8px;align-items:center;font-size:12px;color:#cfe6ef}.health-row span{font-weight:700}.health-row b{font-size:12px;color:#fff}.health-row i{grid-column:1/3;height:9px;background:rgba(255,255,255,.075);border-radius:999px;overflow:hidden}.health-row i em{display:block;height:100%;border-radius:999px;background:linear-gradient(90deg,#34d399,#5eead4,#67e8a5);box-shadow:0 0 14px rgba(94,234,212,.38);animation:flowBar 3.8s linear infinite;background-size:180% 100%}
@keyframes flowBar{from{background-position:0 0}to{background-position:180% 0}}
.timeline-live{display:grid;gap:10px;margin-bottom:12px}.event-line{display:grid;grid-template-columns:48px 1fr auto;gap:10px;align-items:center;border:1px solid rgba(94,234,212,.13);background:rgba(255,255,255,.045);border-radius:16px;padding:11px}.event-line b{color:#a7cfc4;font-size:12px}.event-line span{font-size:12px;color:#f1fbff;font-weight:700}.event-line em{font-style:normal;font-size:9px;font-weight:900;color:#b8ffd6;border:1px solid rgba(103,232,165,.28);border-radius:999px;padding:4px 7px;background:rgba(103,232,165,.08)}
.compact-ai{margin-top:12px;margin-bottom:0!important}.compact-ai .ai-text{font-size:13px;}
.asset-live-grid{display:grid;grid-template-columns:1fr;gap:10px;margin-bottom:10px}.asset-live-card{border:1px solid rgba(94,234,212,.18);background:linear-gradient(145deg,rgba(255,255,255,.05),rgba(6,35,42,.30));border-radius:17px;padding:11px;display:grid;grid-template-columns:1fr auto;gap:8px;align-items:center}.asset-live-card b{display:block;font-size:12px;color:#f2fff9}.asset-live-card span{display:block;font-size:19px;font-weight:900;color:#fff;margin-top:3px}.asset-live-card em{font-style:normal;font-size:10px;font-weight:900;color:#b8ffd6;border:1px solid rgba(103,232,165,.24);background:rgba(103,232,165,.08);border-radius:999px;padding:5px 7px;white-space:nowrap}.asset-live-card.watch em{color:#ffd166;border-color:rgba(255,209,102,.35);background:rgba(255,209,102,.08)}
@keyframes panelBreath{0%,100%{box-shadow:0 22px 60px rgba(0,0,0,.24),0 0 0 rgba(94,234,212,0)}50%{box-shadow:0 24px 66px rgba(0,0,0,.26),0 0 28px rgba(94,234,212,.10)}}

</style>
''', unsafe_allow_html=True)


def live_number_html(value, amp=None, decimals=None):
    """Render a numeric value as a client-side live span so Streamlit does not rerun the whole page."""
    raw = str(value).strip()
    try:
        base = float(raw.replace(',', ''))
    except Exception:
        return raw
    if decimals is None:
        decimals = len(raw.split('.', 1)[1]) if '.' in raw else 0
        decimals = min(decimals, 2)
    if amp is None:
        amp = max(abs(base) * 0.003, 0.08)
    return f'<span class="hoip-live-number" data-base="{base:.6f}" data-amp="{amp:.6f}" data-decimals="{decimals}">{base:.{decimals}f}</span>'

def icon_for(label):
    l = label.lower()
    rules = [
        (("executive","command","plant","health","status"), "⌂"),
        (("vision","architecture"), "◉"),
        (("subsystem","coverage","map"), "▦"),
        (("generation","energy","output","renewable"), "⚡"),
        (("reservoir","storage","level","hydrology","inflow","outflow"), "∿"),
        (("rain","weather","wind","humidity"), "☔"),
        (("dam","safety","civil","seepage","pore","deformation"), "▰"),
        (("turbine","powerhouse","bearing","vibration","unit"), "⚙"),
        (("electrical","switchyard","grid","frequency","power factor"), "⌁"),
        (("air","pm2.5","pm10","co","no₂"), "◎"),
        (("water quality","quality","ph","turbidity","conductivity","oxygen"), "◍"),
        (("correlation","chain","impact"), "⟲"),
        (("ai","confidence","recommendation","advisory"), "✦"),
        (("maintenance","o&m","risk","downtime"), "⚒"),
        (("report","esg","compliance","co₂"), "▣"),
        (("implementation","roadmap","rollout","integration"), "◇"),
    ]
    for keys, ic in rules:
        if any(k in l for k in keys):
            return ic
    return "•"

def live_client_script():
    components.html("""
    <script>
    const parentDoc = window.parent.document;
    function fmt(x, d){ return Number(x).toLocaleString('en-US',{minimumFractionDigits:d, maximumFractionDigits:d}); }
    function updateLiveNumbers(){
      const now = Date.now()/1000;
      parentDoc.querySelectorAll('.hoip-live-number').forEach((el, idx)=>{
        const base = parseFloat(el.dataset.base || '0');
        const amp = parseFloat(el.dataset.amp || '0');
        const dec = parseInt(el.dataset.decimals || '0');
        const wave = Math.sin(now/5.4 + idx*0.71) + 0.25*Math.sin(now/2.7 + idx*1.31);
        const val = base + amp*wave;
        el.textContent = fmt(val, dec);
      });
      const d = new Date();
      const timeOnly = d.toLocaleTimeString('en-GB', {hour:'2-digit', minute:'2-digit', second:'2-digit'});
      parentDoc.querySelectorAll('.hoip-live-clock').forEach(el=>{
        el.textContent = 'Live Simulation • ' + d.toLocaleString('en-GB', {day:'2-digit', month:'short', year:'numeric', hour:'2-digit', minute:'2-digit', second:'2-digit'}).replace(',', '');
      });
      parentDoc.querySelectorAll('.hoip-updated-time').forEach(el=>{ el.textContent = timeOnly; });
    }
    updateLiveNumbers();
    if(!window.__hoipLiveNoReload){ window.__hoipLiveNoReload = setInterval(updateLiveNumbers, 2000); }
    </script>
    """, height=0)

def ai_insight_banner():
    st.markdown("""
    <div class="ai-insight-banner">
      <div class="ai-insight-track">
        <span class="ai-insight"><b>AI Insight:</b> Inflow meningkat 3.2% dalam 15 menit terakhir. Tidak diperlukan perubahan bukaan spillway.</span>
        <span class="ai-insight amber"><b>AI Insight:</b> Piezometer PZ-07 menunjukkan tren naik ringan. Tingkatkan frekuensi observasi bila hujan berlanjut &gt; 48 jam.</span>
        <span class="ai-insight"><b>AI Insight:</b> Unit #2 bekerja pada efisiensi optimum. Tidak ada indikasi overload.</span>
        <span class="ai-insight"><b>AI Insight:</b> Reservoir tetap berada dalam operating rule curve. Dispatch Unit #1–#3 dapat dipertahankan.</span>
        <span class="ai-insight"><b>AI Insight:</b> Inflow meningkat 3.2% dalam 15 menit terakhir. Tidak diperlukan perubahan bukaan spillway.</span>
        <span class="ai-insight amber"><b>AI Insight:</b> Piezometer PZ-07 menunjukkan tren naik ringan. Tingkatkan frekuensi observasi bila hujan berlanjut &gt; 48 jam.</span>
        <span class="ai-insight"><b>AI Insight:</b> Unit #2 bekerja pada efisiensi optimum. Tidak ada indikasi overload.</span>
        <span class="ai-insight"><b>AI Insight:</b> Reservoir tetap berada dalam operating rule curve. Dispatch Unit #1–#3 dapat dipertahankan.</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

def topbar():
    st.markdown(f'''
    <div class="hoip-topbar">
      <div class="hoip-brand">
        <img class="khn-logo" src="data:image/png;base64,{KHN_LOGO_B64}" />
        <div class="brand-divider"></div>
        <div>
          <div class="brand-title">HOIP <span style="color:#5eead4;font-weight:700;">|</span> Hydropower Operational Intelligence Platform</div>
          <div class="brand-subtitle">PT Kayan Hydropower Nusantara • Integrated Intelligence for Safe, Efficient, and Sustainable Hydropower Operations</div>
        </div>
      </div>
      <div style="text-align:right;position:relative;z-index:1;min-width:220px;">
        <div class="status-pill"><span class="pulse"></span> PLANT STATUS: NORMAL</div>
        <div class="hoip-live-clock" style="color:#a7cfc4;font-size:12px;margin-top:7px;">Live Simulation • {datetime.now().strftime('%d %b %Y %H:%M:%S')}</div>
      </div>
    </div>
    ''', unsafe_allow_html=True)
    live_client_script()

def kpi(label, value, unit="", note=""):
    icon = icon_for(label)
    live_val = live_number_html(value)
    st.markdown(f"""
    <div class="kpi-card">
      <div class="kpi-label"><span class="kpi-icon">{icon}</span>{label}</div>
      <div class="kpi-value">{live_val}<span class="kpi-unit">{unit}</span></div>
      <div class="kpi-note">{note}</div>
      <div class="live-updated">Updated <span class="hoip-updated-time">{datetime.now().strftime('%H:%M:%S')}</span></div>
      <div class="live-spark"></div>
    </div>
    """, unsafe_allow_html=True)

def header(title, sub=""):
    st.markdown(f'<div class="panel-title"><h3>{title}</h3><span>{sub}</span></div>', unsafe_allow_html=True)

def metric(name, value):
    st.markdown(f'<div class="metric-row"><div class="metric-name"><span class="metric-icon">{icon_for(name)}</span>{name}</div><div class="metric-value">{live_number_html(value)}</div></div>', unsafe_allow_html=True)

def bar(label, val, color="#34d399"):
    val = max(0, min(100, val))
    st.markdown(f'''
    <div style="margin:10px 0;">
      <div style="display:flex;justify-content:space-between;font-size:12px;color:#bfd7eb;margin-bottom:5px;"><span>{label}</span><b>{val:.1f}%</b></div>
      <div style="height:9px;background:rgba(255,255,255,.08);border-radius:999px;overflow:hidden;">
        <div style="width:{val:.1f}%;height:100%;background:linear-gradient(90deg,{color},#5eead4);border-radius:999px;"></div>
      </div>
    </div>
    ''', unsafe_allow_html=True)

def digital_dam_svg():
    reservoir_pct = data["reservoir_pct"]
    level = data["reservoir_level"]
    generation = data["generation"]
    inflow = data["inflow"]
    outflow = data["outflow"]
    water_y = max(70, min(120, 118 - (reservoir_pct - 70) * 1.4))
    gate_open = max(8, min(34, (outflow-650)/4))
    speed = max(3, 9 - (generation-1100)/70)
    return f'''
<div class="panel" style="height:560px; padding:0; overflow:hidden;">
<svg width="100%" height="560" viewBox="0 0 1050 560" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" x2="1" y1="0" y2="1"><stop offset="0%" stop-color="#0d2440"/><stop offset="55%" stop-color="#071524"/><stop offset="100%" stop-color="#06101d"/></linearGradient>
    <linearGradient id="water" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stop-color="#43e0ff" stop-opacity=".82"/><stop offset="45%" stop-color="#2dd4bf" stop-opacity=".72"/><stop offset="100%" stop-color="#083b77" stop-opacity=".96"/></linearGradient>
    <linearGradient id="dam" x1="0" x2="1"><stop offset="0%" stop-color="#6f7f91"/><stop offset="45%" stop-color="#c5d0da"/><stop offset="100%" stop-color="#718397"/></linearGradient>
    <linearGradient id="penstock" x1="0" x2="1"><stop offset="0%" stop-color="#294b6b"/><stop offset="55%" stop-color="#65b6e8"/><stop offset="100%" stop-color="#19344f"/></linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="4" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <pattern id="flow" width="34" height="10" patternUnits="userSpaceOnUse"><rect width="34" height="10" fill="transparent"/><path d="M0 5 L18 5" stroke="#9cecff" stroke-width="3" stroke-linecap="round" opacity=".75"><animate attributeName="x" from="-34" to="34" dur="{speed:.1f}s" repeatCount="indefinite"/></path></pattern>
    <pattern id="wave" width="120" height="18" patternUnits="userSpaceOnUse"><path d="M0 8 C25 -2, 42 18, 65 8 S105 2, 120 8" fill="none" stroke="#b9f4ff" stroke-width="2" opacity=".45"><animateTransform attributeName="transform" type="translate" from="0 0" to="-120 0" dur="7s" repeatCount="indefinite"/></path><path d="M12 13 C40 5, 60 19, 85 12 S118 9, 132 13" fill="none" stroke="#e0ffff" stroke-width="1.1" opacity=".35"><animateTransform attributeName="transform" type="translate" from="-30 0" to="-150 0" dur="9s" repeatCount="indefinite"/></path></pattern>
  </defs>
  <rect x="0" y="0" width="1050" height="560" fill="url(#sky)"/>
  <circle cx="156" cy="76" r="124" fill="#5eead4" opacity=".08"/>
  <circle cx="880" cy="88" r="150" fill="#37bdf8" opacity=".09"/>
  <path d="M0 235 L150 95 L285 240 L410 118 L590 248 L730 98 L1050 250 L1050 560 L0 560 Z" fill="#0d2338" opacity=".88"/>
  <path d="M0 280 L200 160 L350 290 L560 150 L790 292 L1050 148 L1050 560 L0 560 Z" fill="#0a1c2f" opacity=".92"/>
  <path d="M0 {water_y:.1f} C190 {water_y-12:.1f}, 325 {water_y+12:.1f}, 455 {water_y:.1f} L455 390 L0 390 Z" fill="url(#water)" opacity=".92"/>
  <rect x="0" y="{water_y-5:.1f}" width="455" height="36" fill="url(#wave)" opacity=".95"/>
  <g opacity=".55" filter="url(#glow)">
    <ellipse cx="105" cy="{water_y+18:.1f}" rx="52" ry="5" fill="none" stroke="#d7ffff" stroke-width="1.3"><animate attributeName="rx" values="24;62;24" dur="5.2s" repeatCount="indefinite"/><animate attributeName="opacity" values=".15;.62;.15" dur="5.2s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="260" cy="{water_y+10:.1f}" rx="34" ry="4" fill="none" stroke="#a7f3d0" stroke-width="1.2"><animate attributeName="rx" values="18;48;18" dur="4.5s" repeatCount="indefinite"/><animate attributeName="opacity" values=".12;.55;.12" dur="4.5s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="380" cy="{water_y+23:.1f}" rx="42" ry="4" fill="none" stroke="#7dd3fc" stroke-width="1.2"><animate attributeName="rx" values="18;55;18" dur="6.1s" repeatCount="indefinite"/><animate attributeName="opacity" values=".10;.48;.10" dur="6.1s" repeatCount="indefinite"/></ellipse>
  </g>
  <text x="30" y="{water_y-18:.1f}" fill="#c8f7ff" font-size="16" font-weight="800">Reservoir EL {level:.2f} m</text>
  <text x="30" y="{water_y+11:.1f}" fill="#86dfff" font-size="12">Operational Storage {reservoir_pct:.1f}%</text>
  <path d="M455 112 L585 112 L690 485 L350 485 Z" fill="url(#dam)" opacity=".96"/>
  <path d="M474 126 L570 126 L648 452 L394 452 Z" fill="#dce5ed" opacity=".11"/>
  <path d="M455 112 L585 112 L690 485 L350 485 Z" fill="none" stroke="#ffffff" stroke-opacity=".18" stroke-width="2"/>
  <path d="M465 170 L605 170 M442 250 L630 250 M413 335 L655 335 M382 420 L675 420" stroke="#1b3147" stroke-width="2" opacity=".28"/>
  <text x="438" y="86" fill="#eef8ff" font-size="20" font-weight="900">Digital Dam Twin</text>
  <text x="438" y="105" fill="#a7cfc4" font-size="12">Dam body instrumentation • seepage • pore pressure • deformation</text>
  <g filter="url(#glow)">
    <circle cx="502" cy="184" r="8" fill="#67e8a5"/>
    <circle cx="545" cy="256" r="8" fill="#67e8a5"/>
    <circle cx="480" cy="322" r="8" fill="#ffd166"/>
    <circle cx="602" cy="392" r="8" fill="#67e8a5"/>
  </g>
  <text x="515" y="188" fill="#dff7ff" font-size="11">PZ-07</text><text x="558" y="260" fill="#dff7ff" font-size="11">JM-02</text><text x="493" y="326" fill="#dff7ff" font-size="11">SP-04</text><text x="615" y="396" fill="#dff7ff" font-size="11">TL-01</text>
  <rect x="563" y="130" width="32" height="{gate_open:.1f}" rx="4" fill="#5eead4" opacity=".78"/>
  <g filter="url(#glow)">
    <circle r="3.4" fill="#e0ffff" opacity=".88"><animateMotion dur="1.3s" repeatCount="indefinite" path="M430 137 C480 130, 530 132, 590 {130+gate_open:.1f}"/></circle>
    <circle r="2.8" fill="#5eead4" opacity=".82"><animateMotion dur="1.7s" begin=".35s" repeatCount="indefinite" path="M410 152 C475 144, 535 142, 590 {130+gate_open:.1f}"/></circle>
    <circle r="2.4" fill="#ffffff" opacity=".70"><animateMotion dur="1.9s" begin=".7s" repeatCount="indefinite" path="M388 166 C470 154, 535 150, 590 {130+gate_open:.1f}"/></circle>
  </g>
  <path d="M590 {130+gate_open:.1f} C650 190, 650 280, 725 330" stroke="#7feaff" stroke-width="13" opacity=".50" fill="none" stroke-linecap="round"/>
  <path d="M590 {130+gate_open:.1f} C650 190, 650 280, 725 330" stroke="url(#flow)" stroke-width="7" opacity=".95" fill="none" stroke-linecap="round"/>
  <path d="M535 260 C660 285, 705 360, 776 426" stroke="#142b43" stroke-width="33" fill="none" stroke-linecap="round"/>
  <path d="M535 260 C660 285, 705 360, 776 426" stroke="url(#penstock)" stroke-width="26" fill="none" stroke-linecap="round"/>
  <path d="M535 260 C660 285, 705 360, 776 426" stroke="url(#flow)" stroke-width="12" fill="none" stroke-linecap="round" opacity=".78"/>
  <g filter="url(#glow)">
    <circle r="5" fill="#bffaff" opacity=".95"><animateMotion dur="1.7s" repeatCount="indefinite" path="M535 260 C660 285, 705 360, 776 426"/></circle>
    <circle r="4" fill="#5eead4" opacity=".90"><animateMotion dur="2.4s" begin=".55s" repeatCount="indefinite" path="M535 260 C660 285, 705 360, 776 426"/></circle>
    <circle r="3" fill="#ffffff" opacity=".80"><animateMotion dur="2.4s" begin="1.1s" repeatCount="indefinite" path="M535 260 C660 285, 705 360, 776 426"/></circle>
  </g>
  <rect x="735" y="380" width="220" height="96" rx="18" fill="rgba(16,36,60,.88)" stroke="#5eead4" stroke-opacity=".18"/>
  <rect x="754" y="402" width="52" height="52" rx="13" fill="#12304e" stroke="#67e8a5" stroke-opacity=".45"/><rect x="820" y="402" width="52" height="52" rx="13" fill="#12304e" stroke="#67e8a5" stroke-opacity=".45"/><rect x="886" y="402" width="52" height="52" rx="13" fill="#12304e" stroke="#67e8a5" stroke-opacity=".45"/>
  <circle class="unit-live" cx="780" cy="428" r="17" fill="#67e8a5" opacity=".58"><animate attributeName="r" values="14;18;14" dur="1.35s" repeatCount="indefinite"/><animate attributeName="opacity" values=".45;1;.45" dur="1.35s" repeatCount="indefinite"/></circle><circle class="unit-live" cx="846" cy="428" r="17" fill="#67e8a5" opacity=".58"><animate attributeName="r" values="14;18;14" dur="1.45s" repeatCount="indefinite"/><animate attributeName="opacity" values=".45;1;.45" dur="1.45s" repeatCount="indefinite"/></circle><circle class="unit-live" cx="912" cy="428" r="17" fill="#67e8a5" opacity=".58"><animate attributeName="r" values="14;18;14" dur="1.55s" repeatCount="indefinite"/><animate attributeName="opacity" values=".45;1;.45" dur="1.55s" repeatCount="indefinite"/></circle>
  <text x="750" y="368" fill="#eef8ff" font-size="16" font-weight="800">Powerhouse</text><text x="754" y="468" fill="#b8ffd6" font-size="11" font-weight="900">U1 ON</text><text x="820" y="468" fill="#b8ffd6" font-size="11" font-weight="900">U2 ON</text><text x="886" y="468" fill="#b8ffd6" font-size="11" font-weight="900">U3 ON</text><text x="760" y="397" fill="#a7cfc4" font-size="10">Generation</text><text x="836" y="397" fill="#ffffff" font-size="18" font-weight="900"><tspan class="hoip-live-number svg-live-num" data-base="{generation:.0f}" data-amp="22" data-decimals="0">{generation:.0f}</tspan> MW</text>
  <rect x="760" y="126" width="225" height="132" rx="18" fill="rgba(12,28,49,.76)" stroke="#5eead4" stroke-opacity=".17"/>
  <text x="778" y="153" fill="#eef8ff" font-size="16" font-weight="900">Switchyard</text><line x1="788" y1="198" x2="958" y2="198" stroke="#5eead4" stroke-width="3" opacity=".65"/>
  <circle cx="812" cy="198" r="9" fill="#67e8a5"/><circle cx="866" cy="198" r="9" fill="#67e8a5"/><circle cx="920" cy="198" r="9" fill="#67e8a5"/>
  <line x1="812" y1="198" x2="812" y2="230" stroke="#5eead4" stroke-width="2" opacity=".65"/><line x1="866" y1="198" x2="866" y2="230" stroke="#5eead4" stroke-width="2" opacity=".65"/><line x1="920" y1="198" x2="920" y2="230" stroke="#5eead4" stroke-width="2" opacity=".65"/>
  <rect x="796" y="230" width="32" height="14" rx="4" fill="#2dd4bf" opacity=".65"/><rect x="850" y="230" width="32" height="14" rx="4" fill="#2dd4bf" opacity=".65"/><rect x="904" y="230" width="32" height="14" rx="4" fill="#2dd4bf" opacity=".65"/>
  <path d="M958 198 C995 195, 1018 176, 1050 174" stroke="url(#flow)" stroke-width="5" opacity=".88"/>
  <g opacity=".78">
    <path d="M780 458 C840 493, 925 500, 1050 492" stroke="#5eead4" stroke-width="10" fill="none" stroke-linecap="round" opacity=".22"/>
    <path d="M780 458 C840 493, 925 500, 1050 492" stroke="url(#flow)" stroke-width="5" fill="none" stroke-linecap="round" opacity=".82"/>
    <text x="865" y="520" fill="#9fe7d3" font-size="12" font-weight="800">Tailrace flow • discharge stabilized</text>
  </g>
  <rect x="30" y="405" width="265" height="82" rx="18" fill="rgba(3,22,28,.66)" stroke="#5eead4" stroke-opacity=".18"/>
  <text x="50" y="432" fill="#a7cfc4" font-size="12">Hydrology</text><text x="50" y="459" fill="#eef8ff" font-size="25" font-weight="900">Inflow <tspan class="hoip-live-number svg-live-num" data-base="{inflow:.0f}" data-amp="38" data-decimals="0">{inflow:.0f}</tspan> m³/s</text><text x="50" y="478" fill="#a7cfc4" font-size="12">Outflow <tspan class="hoip-live-number" data-base="{outflow:.0f}" data-amp="24" data-decimals="0">{outflow:.0f}</tspan> m³/s • Water balance positive</text>
</svg></div>
'''

def powerhouse_svg():
    gen = data["generation"]
    vib = data["vib"]
    temp = data["bearing_temp"]
    oil = live(5.4,.2,24,.02)
    cool = live(320,15,26,2)
    rpm = live(300,.7,13,.08)
    blade_durs = ["3.8s", "3.3s", "4.1s"]
    units = ""
    for i, dur in enumerate(blade_durs):
        x = 390 + i * 145
        mw = 388 + i * 14 + math.sin(t/(12+i))*7
        width = 64 + i*2
        units += f"""<g transform=\"translate({x},278)\" filter=\"url(#halo)\">
<circle cx=\"0\" cy=\"0\" r=\"48\" fill=\"#031a18\" stroke=\"#34d399\" stroke-width=\"2.5\" opacity=\".96\"/>
<circle cx=\"0\" cy=\"0\" r=\"36\" fill=\"#0b3b34\" stroke=\"#5eead4\" stroke-opacity=\".45\" stroke-width=\"1.5\"/>
<g>
<path d=\"M0 -34 C12 -24 14 -9 4 -2 C24 3 33 15 35 29 C18 27 5 18 1 5 C-10 23 -24 30 -38 30 C-28 15 -17 5 -4 1 C-24 -5 -34 -17 -36 -30 C-19 -28 -6 -18 0 -4 Z\" fill=\"url(#blade)\" opacity=\".92\"/>
<animateTransform attributeName=\"transform\" type=\"rotate\" from=\"0\" to=\"360\" dur=\"{dur}\" repeatCount=\"indefinite\"/>
</g>
<circle cx=\"0\" cy=\"0\" r=\"9\" fill=\"#dffbf1\" opacity=\".9\"/>
<circle cx=\"0\" cy=\"0\" r=\"5\" fill=\"#22c55e\"/>
<text x=\"0\" y=\"77\" text-anchor=\"middle\" fill=\"#eef8ff\" font-size=\"13\" font-weight=\"900\">UNIT {i+1}</text>
<text x=\"0\" y=\"96\" text-anchor=\"middle\" fill=\"#9fe7d3\" font-size=\"12\" font-weight=\"700\">{mw:.0f} MW</text>
<rect x=\"-36\" y=\"110\" width=\"72\" height=\"9\" rx=\"5\" fill=\"#06231f\" stroke=\"#14594c\"/>
<rect x=\"-36\" y=\"110\" width=\"{width}\" height=\"9\" rx=\"5\" fill=\"#34d399\" opacity=\".85\"/>
</g>"""
    return f"""<style>html,body{{margin:0;background:transparent;overflow:hidden;font-family:Inter,Arial,sans-serif;}}</style>
<svg width=\"100%\" height=\"535\" viewBox=\"0 0 940 535\" xmlns=\"http://www.w3.org/2000/svg\">
<defs>
<linearGradient id=\"bgph\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\"><stop offset=\"0%\" stop-color=\"#021b15\"/><stop offset=\"45%\" stop-color=\"#062c27\"/><stop offset=\"100%\" stop-color=\"#061421\"/></linearGradient>
<linearGradient id=\"waterPipe\" x1=\"0\" x2=\"1\"><stop offset=\"0\" stop-color=\"#0a2a41\"/><stop offset=\".34\" stop-color=\"#2dd4bf\"/><stop offset=\".62\" stop-color=\"#67e8f9\"/><stop offset=\"1\" stop-color=\"#0e3348\"/></linearGradient>
<linearGradient id=\"blade\" x1=\"0\" x2=\"1\"><stop offset=\"0\" stop-color=\"#22c55e\"/><stop offset=\".55\" stop-color=\"#67e8f9\"/><stop offset=\"1\" stop-color=\"#dffbf1\"/></linearGradient>
<pattern id=\"flowDash\" width=\"54\" height=\"12\" patternUnits=\"userSpaceOnUse\"><path d=\"M3 6 L31 6\" stroke=\"#d8ffff\" stroke-width=\"3\" stroke-linecap=\"round\" opacity=\".9\"><animate attributeName=\"x\" from=\"-54\" to=\"54\" dur=\"2.2s\" repeatCount=\"indefinite\"/></path></pattern>
<filter id=\"halo\"><feGaussianBlur stdDeviation=\"4\" result=\"b\"/><feMerge><feMergeNode in=\"b\"/><feMergeNode in=\"SourceGraphic\"/></feMerge></filter>
<filter id=\"soft\"><feDropShadow dx=\"0\" dy=\"16\" stdDeviation=\"18\" flood-color=\"#000\" flood-opacity=\".35\"/></filter>
</defs>
<rect width=\"940\" height=\"535\" rx=\"28\" fill=\"url(#bgph)\"/>
<circle cx=\"145\" cy=\"90\" r=\"145\" fill=\"#10b981\" opacity=\".08\"/>
<circle cx=\"820\" cy=\"80\" r=\"190\" fill=\"#5eead4\" opacity=\".07\"/>
<path d=\"M35 126 C145 112,210 143,310 222 C372 270,432 293,500 293\" stroke=\"#0b2740\" stroke-width=\"58\" fill=\"none\" stroke-linecap=\"round\" opacity=\".95\"/>
<path d=\"M35 126 C145 112,210 143,310 222 C372 270,432 293,500 293\" stroke=\"url(#waterPipe)\" stroke-width=\"42\" fill=\"none\" stroke-linecap=\"round\" opacity=\".95\"/>
<path d=\"M35 126 C145 112,210 143,310 222 C372 270,432 293,500 293\" stroke=\"url(#flowDash)\" stroke-width=\"20\" fill=\"none\" stroke-linecap=\"round\" opacity=\".75\"/>
<path d=\"M115 148 C205 172,285 235,350 285\" stroke=\"#7dd3fc\" stroke-width=\"3\" fill=\"none\" opacity=\".35\" stroke-dasharray=\"18 18\"><animate attributeName=\"stroke-dashoffset\" from=\"80\" to=\"0\" dur=\"2.4s\" repeatCount=\"indefinite\"/></path>
<rect x=\"315\" y=\"150\" width=\"540\" height=\"270\" rx=\"32\" fill=\"#071f31\" stroke=\"#1f8f7a\" stroke-opacity=\".62\" filter=\"url(#soft)\"/>
<rect x=\"338\" y=\"183\" width=\"494\" height=\"205\" rx=\"24\" fill=\"#0b2637\" stroke=\"#5eead4\" stroke-opacity=\".18\"/>
<text x=\"346\" y=\"192\" fill=\"#eef8ff\" font-size=\"22\" font-weight=\"900\">Powerhouse Unit Bay</text>
<text x=\"346\" y=\"217\" fill=\"#9fe7d3\" font-size=\"13\">Penstock flow • turbine rotation • generator loading • cooling/oil condition</text>
<line x1=\"352\" y1=\"245\" x2=\"808\" y2=\"245\" stroke=\"#5eead4\" stroke-opacity=\".18\"/>
{units}
<rect x=\"52\" y=\"386\" width=\"255\" height=\"92\" rx=\"22\" fill=\"#061e2b\" stroke=\"#22c55e\" stroke-opacity=\".35\"/>
<text x=\"78\" y=\"418\" fill=\"#9fe7d3\" font-size=\"12\" font-weight=\"800\">HYDRAULIC DRIVE</text>
<text x=\"78\" y=\"450\" fill=\"#eef8ff\" font-size=\"30\" font-weight=\"900\">{gen:.0f}<tspan font-size=\"16\"> MW</tspan></text>
<text x=\"78\" y=\"470\" fill=\"#34d399\" font-size=\"12\" font-weight=\"700\">3 units synchronized • water-to-energy stable</text>
<rect x=\"330\" y=\"438\" width=\"555\" height=\"54\" rx=\"18\" fill=\"#061e2b\" stroke=\"#5eead4\" stroke-opacity=\".20\"/>
<text x=\"356\" y=\"470\" fill=\"#9fe7d3\" font-size=\"12\">RPM</text><text x=\"405\" y=\"470\" fill=\"#eef8ff\" font-size=\"18\" font-weight=\"900\">{rpm:.1f}</text>
<text x=\"512\" y=\"470\" fill=\"#9fe7d3\" font-size=\"12\">Vibration</text><text x=\"600\" y=\"470\" fill=\"#eef8ff\" font-size=\"18\" font-weight=\"900\">{vib:.2f} mm/s</text>
<text x=\"735\" y=\"470\" fill=\"#9fe7d3\" font-size=\"12\">Bearing</text><text x=\"810\" y=\"470\" fill=\"#eef8ff\" font-size=\"18\" font-weight=\"900\">{temp:.1f}°C</text>
<rect x=\"715\" y=\"58\" width=\"170\" height=\"78\" rx=\"20\" fill=\"#05251f\" stroke=\"#34d399\" stroke-opacity=\".35\"/>
<text x=\"738\" y=\"90\" fill=\"#9fe7d3\" font-size=\"12\" font-weight=\"800\">OIL / COOLING</text>
<text x=\"738\" y=\"116\" fill=\"#eef8ff\" font-size=\"17\" font-weight=\"900\">{oil:.2f} bar • {cool:.0f} L/min</text>
<circle cx=\"895\" cy=\"42\" r=\"9\" fill=\"#34d399\" opacity=\".88\"><animate attributeName=\"r\" values=\"8;13;8\" dur=\"1.8s\" repeatCount=\"indefinite\"/><animate attributeName=\"opacity\" values=\".95;.35;.95\" dur=\"1.8s\" repeatCount=\"indefinite\"/></circle>
</svg>"""

def electrical_svg():
    freq = data['freq']
    pf = data['pf']
    eh = data['electrical_health']
    sh = data['switchyard_health']
    gen = data['generation']
    tr_temp = live(58.3, 1.2, 21, .1)
    arrester = live(.42, .04, 19, .01)
    load_pct = max(42, min(96, 62 + (gen - 1120) / 8))
    return f"""<svg width="100%" height="560" viewBox="0 0 980 560" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="elecBg" x1="0" x2="1" y1="0" y2="1">
    <stop offset="0%" stop-color="#05251f"/><stop offset="58%" stop-color="#071c25"/><stop offset="100%" stop-color="#031018"/>
  </linearGradient>
  <linearGradient id="panelGlass" x1="0" x2="1" y1="0" y2="1">
    <stop offset="0%" stop-color="#0b4337" stop-opacity=".88"/><stop offset="100%" stop-color="#071827" stop-opacity=".72"/>
  </linearGradient>
  <linearGradient id="busGlow" x1="0" x2="1">
    <stop offset="0%" stop-color="#34d399"/><stop offset="55%" stop-color="#5eead4"/><stop offset="100%" stop-color="#38bdf8"/>
  </linearGradient>
  <pattern id="powerFlow" width="48" height="10" patternUnits="userSpaceOnUse">
    <rect width="48" height="10" fill="transparent"/>
    <path d="M0 5 L26 5" stroke="#b9fff1" stroke-width="3.5" stroke-linecap="round" opacity=".95">
      <animate attributeName="x" from="-48" to="48" dur="2.5s" repeatCount="indefinite"/>
    </path>
  </pattern>
  <filter id="softElecGlow"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="strongGlow"><feGaussianBlur stdDeviation="8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="980" height="560" rx="30" fill="url(#elecBg)"/>
<circle cx="110" cy="90" r="150" fill="#34d399" opacity=".06"/>
<circle cx="865" cy="110" r="185" fill="#38bdf8" opacity=".07"/>
<path d="M0 410 C170 345,245 390,365 330 C515 255,680 315,980 220 L980 560 L0 560 Z" fill="#063225" opacity=".32"/>
<text x="44" y="58" fill="#eef8ff" font-size="24" font-weight="900">Electrical Intelligence Layer</text>
<text x="44" y="84" fill="#a7cfc4" font-size="13">Animated single-line diagram - generator to transformer to switchyard to grid export</text>
<g filter="url(#softElecGlow)">
  <rect x="42" y="126" width="160" height="268" rx="26" fill="url(#panelGlass)" stroke="#5eead4" stroke-opacity=".22"/>
  <text x="72" y="160" fill="#9fe7d3" font-size="12" font-weight="900">GENERATOR BAY</text>
  <g transform="translate(122,215)">
    <circle r="48" fill="#05251f" stroke="#34d399" stroke-width="3"/>
    <circle r="27" fill="#34d399" opacity=".16"/>
    <path d="M0 -38 L10 -8 L38 0 L10 8 L0 38 L-10 8 L-38 0 L-10 -8 Z" fill="#9fffd0" opacity=".62">
      <animateTransform attributeName="transform" attributeType="XML" type="rotate" from="0" to="360" dur="4.2s" repeatCount="indefinite"/>
    </path>
    <text x="-18" y="88" fill="#eef8ff" font-size="15" font-weight="900">G1</text>
  </g>
  <g transform="translate(122,330)">
    <circle r="38" fill="#05251f" stroke="#5eead4" stroke-width="3"/>
    <text x="-20" y="5" fill="#eef8ff" font-size="16" font-weight="900">AVR</text>
    <circle r="52" fill="none" stroke="#34d399" stroke-opacity=".25" stroke-width="2"><animate attributeName="r" values="46;58;46" dur="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values=".85;.2;.85" dur="2.4s" repeatCount="indefinite"/></circle>
  </g>
</g>
<line x1="202" y1="215" x2="330" y2="215" stroke="url(#powerFlow)" stroke-width="7" stroke-linecap="round"/>
<line x1="202" y1="330" x2="330" y2="330" stroke="url(#powerFlow)" stroke-width="5" stroke-linecap="round" opacity=".75"/>
<g filter="url(#softElecGlow)">
  <rect x="330" y="125" width="210" height="270" rx="30" fill="url(#panelGlass)" stroke="#5eead4" stroke-opacity=".24"/>
  <text x="372" y="160" fill="#eef8ff" font-size="20" font-weight="900">GSU Transformer</text>
  <text x="386" y="183" fill="#a7cfc4" font-size="12">13.8 kV to 275 kV step-up</text>
  <circle cx="435" cy="248" r="56" fill="#061e2b" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="435" cy="304" r="56" fill="#061e2b" stroke="#34d399" stroke-width="3"/>
  <path d="M395 248 C420 220,450 276,475 248" fill="none" stroke="#b9fff1" stroke-width="4" opacity=".85"><animate attributeName="opacity" values=".35;1;.35" dur="1.8s" repeatCount="indefinite"/></path>
  <path d="M395 304 C420 276,450 332,475 304" fill="none" stroke="#b9fff1" stroke-width="4" opacity=".75"><animate attributeName="opacity" values="1;.35;1" dur="1.8s" repeatCount="indefinite"/></path>
  <rect x="368" y="348" width="134" height="28" rx="14" fill="#05251f" stroke="#34d399" stroke-opacity=".28"/>
  <text x="386" y="367" fill="#9fe7d3" font-size="12" font-weight="800">Oil {tr_temp:.1f} C</text>
</g>
<line x1="540" y1="260" x2="625" y2="260" stroke="url(#powerFlow)" stroke-width="8" stroke-linecap="round"/>
<g filter="url(#softElecGlow)">
  <rect x="625" y="118" width="285" height="300" rx="32" fill="url(#panelGlass)" stroke="#5eead4" stroke-opacity=".26"/>
  <text x="660" y="154" fill="#eef8ff" font-size="20" font-weight="900">Switchyard 275 kV</text>
  <text x="660" y="177" fill="#a7cfc4" font-size="12">Breaker - arrester - busbar - export feeder</text>
  <line x1="670" y1="244" x2="860" y2="244" stroke="url(#busGlow)" stroke-width="5" stroke-linecap="round"/>
  <circle cx="700" cy="244" r="11" fill="#34d399"/><line x1="700" y1="244" x2="700" y2="314" stroke="#5eead4" stroke-width="3"/><rect x="681" y="314" width="38" height="18" rx="5" fill="#38bdf8" opacity=".80"/>
  <circle cx="765" cy="244" r="11" fill="#34d399"/><line x1="765" y1="244" x2="765" y2="314" stroke="#5eead4" stroke-width="3"/><rect x="746" y="314" width="38" height="18" rx="5" fill="#38bdf8" opacity=".80"/>
  <circle cx="830" cy="244" r="11" fill="#34d399"/><line x1="830" y1="244" x2="830" y2="314" stroke="#5eead4" stroke-width="3"/><rect x="811" y="314" width="38" height="18" rx="5" fill="#38bdf8" opacity=".80"/>
  <circle cx="700" cy="244" r="20" fill="none" stroke="#34d399" stroke-opacity=".25" stroke-width="3"><animate attributeName="r" values="15;27;15" dur="2.1s" repeatCount="indefinite"/></circle>
  <circle cx="765" cy="244" r="20" fill="none" stroke="#34d399" stroke-opacity=".25" stroke-width="3"><animate attributeName="r" values="17;30;17" dur="2.4s" repeatCount="indefinite"/></circle>
  <circle cx="830" cy="244" r="20" fill="none" stroke="#34d399" stroke-opacity=".25" stroke-width="3"><animate attributeName="r" values="16;28;16" dur="2.2s" repeatCount="indefinite"/></circle>
</g>
<path d="M910 244 C945 238,955 218,980 215" stroke="url(#powerFlow)" stroke-width="8" stroke-linecap="round"/>
<text x="900" y="205" fill="#9fe7d3" font-size="12" font-weight="900">GRID EXPORT</text>
<g filter="url(#strongGlow)">
  <rect x="45" y="438" width="885" height="72" rx="22" fill="#061e2b" stroke="#5eead4" stroke-opacity=".20"/>
  <text x="75" y="467" fill="#a7cfc4" font-size="13">Generator Voltage</text><text x="205" y="467" fill="#eef8ff" font-size="20" font-weight="900">13.8 kV</text>
  <text x="320" y="467" fill="#a7cfc4" font-size="13">Frequency</text><text x="410" y="467" fill="#eef8ff" font-size="20" font-weight="900">{freq:.2f} Hz</text>
  <text x="525" y="467" fill="#a7cfc4" font-size="13">PF</text><text x="562" y="467" fill="#eef8ff" font-size="20" font-weight="900">{pf:.3f}</text>
  <text x="665" y="467" fill="#a7cfc4" font-size="13">Load</text><text x="716" y="467" fill="#eef8ff" font-size="20" font-weight="900">{load_pct:.1f}%</text>
  <text x="805" y="467" fill="#a7cfc4" font-size="13">Arrester</text><text x="875" y="467" fill="#b8ffd6" font-size="20" font-weight="900">{arrester:.2f}</text>
  <rect x="75" y="488" width="805" height="8" rx="4" fill="#ffffff" opacity=".07"/>
  <rect x="75" y="488" width="{805*eh/100:.1f}" height="8" rx="4" fill="url(#busGlow)" opacity=".92"/>
</g>
<text x="44" y="536" fill="#6ee7c7" font-size="11" opacity=".78">Electrical Health {eh:.1f}% - Switchyard Health {sh:.1f}% - THD 2.1% - CB-02 18 operations - No active trip</text>
</svg>"""

def automation_matrix():
    modules = [
        {"icon":"☁️", "title":"Weather & Catchment", "badge":"AUTO", "coverage":99, "tags":"32 tags", "model":"Hydrology forecast", "health":"ONLINE", "body":"Rainfall, catchment weather, inflow trend, flood early warning, short-term hydrology forecast.", "mon":["Rainfall", "Wind", "Humidity", "Inflow"]},
        {"icon":"💧", "title":"Reservoir & Spillway", "badge":"AUTO + OPERATOR", "coverage":97, "tags":"28 tags", "model":"Water balance", "health":"ONLINE", "body":"Reservoir level, storage curve, gate position, discharge recommendation, operational water balance.", "mon":["Level", "Storage", "Gate", "Outflow"]},
        {"icon":"🏗", "title":"Dam Safety", "badge":"AUTO", "coverage":98, "tags":"41 tags", "model":"Safety index", "health":"ONLINE", "body":"Piezometer, seepage, tilt, joint meter, deformation, structural safety index and anomaly watch.", "mon":["Piezometer", "Seepage", "Tilt", "Joint"]},
        {"icon":"🧪", "title":"Water Quality", "badge":"AUTO + LAB", "coverage":94, "tags":"18 tags", "model":"Compliance watch", "health":"LAB VERIFIED", "body":"pH, turbidity, temperature, conductivity, DO, plus laboratory confirmation for regulatory samples.", "mon":["pH", "Turbidity", "DO", "Conductivity"]},
        {"icon":"🪨", "title":"Sedimentation", "badge":"MANUAL + ANALYTIC", "coverage":86, "tags":"survey layer", "model":"Loss-of-storage", "health":"PERIODIC", "body":"Bathymetry survey upload, sediment trend, sedimentation dashboard and loss-of-storage analytics.", "mon":["Bathymetry", "TSS", "Storage loss", "Trend"]},
        {"icon":"⚙️", "title":"Turbine & Generator", "badge":"AUTO", "coverage":97, "tags":"36 tags", "model":"O&M risk", "health":"ONLINE", "body":"RPM, vibration, bearing temperature, oil pressure, cooling flow, efficiency and maintenance risk.", "mon":["RPM", "Vibration", "Bearing", "Oil"]},
        {"icon":"⚡", "title":"⚡ Electrical & Switchyard", "badge":"AUTO", "coverage":99, "tags":"30 tags", "model":"Power quality", "health":"ONLINE", "body":"Generator, transformer, breaker, protection relay, frequency, PF, THD and export power quality.", "mon":["MW", "PF", "Freq", "Breaker"]},
        {"icon":"🌿", "title":"📊 ESG & Reporting", "badge":"AUTO", "coverage":96, "tags":"12 reports", "model":"Executive KPI", "health":"READY", "body":"Renewable energy, CO₂ avoided, compliance dashboard, executive PDF/Excel reporting.", "mon":["CO₂", "Energy", "Compliance", "KPI"]},
    ]
    html = '<div class="coverage-hero"><div><div class="coverage-eyebrow">SUBSYSTEM COVERAGE MAP</div><div class="coverage-title">End-to-End Hydropower Subsystem Coverage</div><div class="coverage-subtitle">Complete operational visibility across civil, water, turbine, electrical, environmental, governance and executive reporting domains.</div></div><div class="coverage-legend"><span><i class="lg auto"></i>AUTO</span><span><i class="lg op"></i>AUTO + OPERATOR</span><span><i class="lg lab"></i>AUTO + LAB</span><span><i class="lg manual"></i>MANUAL + ANALYTIC</span></div></div><div class="coverage-map-grid">'
    for m in modules:
        cls = 'auto'
        if 'OPERATOR' in m['badge']: cls = 'op'
        if 'LAB' in m['badge']: cls = 'lab'
        if 'MANUAL' in m['badge']: cls = 'manual'
        chips = ''.join([f'<span>{x}</span>' for x in m['mon']])
        spark = ''.join([f'<b style="height:{10 + ((i*7 + m["coverage"])%28)}px"></b>' for i in range(13)])
        html += f'''
        <div class="coverage-card {cls}">
          <div class="coverage-card-top"><div class="cov-icon">{m['icon']}</div><div class="cov-ring" style="--p:{m['coverage']};"><span>{m['coverage']}%</span></div></div>
          <div class="cov-title">{m['title']}</div><div class="cov-body">{m['body']}</div>
          <div class="cov-meta"><div><small>Telemetry</small><strong>{m['tags']}</strong></div><div><small>AI Layer</small><strong>{m['model']}</strong></div><div><small>Status</small><strong>{m['health']}</strong></div></div>
          <div class="cov-chips">{chips}</div><div class="cov-footer"><span class="cov-badge {cls}">{m['badge']}</span><div class="mini-spark">{spark}</div></div>
        </div>'''
    html += '</div><div class="coverage-summary-bar"><div><span>Civil</span><b>100%</b></div><div><span>Water</span><b>98%</b></div><div><span>Mechanical</span><b>97%</b></div><div><span>Electrical</span><b>99%</b></div><div><span>Environmental</span><b>95%</b></div><div><span>Executive</span><b>96%</b></div></div>'
    st.markdown(html, unsafe_allow_html=True)

def intelligence_architecture_svg():
    return '\n    <div class="panel" style="padding:0;overflow:hidden;">\n    <svg width="100%" height="580" viewBox="0 0 1140 580" xmlns="http://www.w3.org/2000/svg">\n      <defs>\n        <linearGradient id="visionGrad" x1="0" x2="1" y1="0" y2="1"><stop offset="0%" stop-color="#0f513f"/><stop offset="100%" stop-color="#082135"/></linearGradient>\n        <linearGradient id="hubGrad" x1="0" x2="1" y1="0" y2="1"><stop offset="0%" stop-color="#0ea5a6" stop-opacity=".92"/><stop offset="55%" stop-color="#07354a" stop-opacity=".94"/><stop offset="100%" stop-color="#061a2a" stop-opacity=".96"/></linearGradient>\n        <linearGradient id="beamGrad" x1="0" x2="1"><stop offset="0%" stop-color="#1dd3b0" stop-opacity=".10"/><stop offset="45%" stop-color="#7df9ff" stop-opacity=".95"/><stop offset="75%" stop-color="#ffd166" stop-opacity=".88"/><stop offset="100%" stop-color="#1dd3b0" stop-opacity=".10"/></linearGradient>\n        <filter id="glowStrong"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>\n        <filter id="softShadow"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000000" flood-opacity=".42"/></filter>\n        <pattern id="dayakMini" width="54" height="54" patternUnits="userSpaceOnUse"><path d="M7 27 Q27 7 47 27 Q27 47 7 27Z" fill="none" stroke="#5eead4" stroke-opacity=".055" stroke-width="2"/><path d="M27 8 L37 27 L27 46 L17 27Z" fill="none" stroke="#ffd166" stroke-opacity=".045" stroke-width="1.5"/></pattern>\n        <pattern id="beamFlow" width="68" height="10" patternUnits="userSpaceOnUse"><rect width="68" height="10" fill="transparent"/><path d="M0 5 L30 5" stroke="url(#beamGrad)" stroke-width="5" stroke-linecap="round"><animate attributeName="x" from="-68" to="68" dur="2.8s" repeatCount="indefinite"/></path></pattern>\n        <style>\n          .smallcap{font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;fill:#8fe7d5;opacity:.92}\n          .titleText{font-size:27px;font-weight:900;fill:#f2fff9;letter-spacing:-.6px}.subText{font-size:13px;fill:#a7cfc4}\n          .nodeTitle{font-size:15px;font-weight:900;fill:#f2fff9;text-anchor:middle}.nodeSub{font-size:11px;fill:#b6d8d0;text-anchor:middle}\n          .pulseNode{animation:nodePulse 2.6s ease-in-out infinite; transform-origin:center; transform-box:fill-box}.ringSpin{animation:ringSpin 16s linear infinite; transform-origin:570px 288px}.ringSpin2{animation:ringSpin 25s linear reverse infinite; transform-origin:570px 288px}\n          @keyframes nodePulse{0%,100%{opacity:.76;filter:drop-shadow(0 0 2px rgba(94,234,212,.25))}50%{opacity:1;filter:drop-shadow(0 0 13px rgba(94,234,212,.72))}}\n          @keyframes ringSpin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}\n        </style>\n      </defs>\n      <rect width="1140" height="580" rx="30" fill="rgba(4,16,24,.42)"/><rect width="1140" height="580" rx="30" fill="url(#dayakMini)"/>\n      <path d="M0 486 C150 430 250 505 396 454 C540 404 660 492 818 440 C944 398 1020 425 1140 390 L1140 580 L0 580Z" fill="#0b2d25" opacity=".34"/>\n      <path d="M0 520 C180 464 300 522 440 485 C600 442 760 535 930 470 C1020 435 1080 448 1140 430" fill="none" stroke="#5eead4" stroke-opacity=".10" stroke-width="2"/>\n      <text x="44" y="52" class="titleText">From Corporate Vision to Operational Excellence</text>\n      <text x="44" y="80" class="subText">HOIP bridges PT Kayan\'s sustainability vision with real-time operational execution, asset reliability, ESG governance, and executive decision support.</text>\n      <g filter="url(#softShadow)"><rect x="44" y="112" width="255" height="155" rx="28" fill="url(#visionGrad)" stroke="#5eead4" stroke-opacity=".22"/><text x="72" y="146" class="smallcap">Corporate Vision</text><text x="76" y="180" fill="#f2fff9" font-size="17" font-weight="900">Sustainable Hydropower</text><text x="76" y="210" fill="#dffbf1" font-size="14">Safe Operation</text><text x="76" y="234" fill="#dffbf1" font-size="14">Reliable Assets</text><text x="76" y="258" fill="#dffbf1" font-size="14">ESG Commitment</text></g>\n      <path d="M300 190 C385 190 430 240 470 264" stroke="url(#beamFlow)" stroke-width="7" fill="none" filter="url(#glowStrong)"/><path d="M300 190 C385 190 430 240 470 264" stroke="#5eead4" stroke-opacity=".16" stroke-width="2" fill="none"/>\n      <g class="ringSpin" opacity=".82"><circle cx="570" cy="288" r="115" fill="none" stroke="#5eead4" stroke-opacity=".24" stroke-width="2" stroke-dasharray="14 12"/><circle cx="570" cy="173" r="4" fill="#ffd166"/><circle cx="685" cy="288" r="4" fill="#5eead4"/><circle cx="570" cy="403" r="4" fill="#67e8a5"/><circle cx="455" cy="288" r="4" fill="#7df9ff"/></g><g class="ringSpin2" opacity=".45"><circle cx="570" cy="288" r="136" fill="none" stroke="#ffd166" stroke-opacity=".13" stroke-width="1.3" stroke-dasharray="6 18"/></g>\n      <g filter="url(#glowStrong)"><polygon points="570,158 682,223 682,353 570,418 458,353 458,223" fill="url(#hubGrad)" stroke="#7df9ff" stroke-opacity=".42" stroke-width="2"/><text x="570" y="268" text-anchor="middle" fill="#f2fff9" font-size="30" font-weight="900">HOIP</text><text x="570" y="296" text-anchor="middle" fill="#b8fff0" font-size="15" font-weight="800">Intelligence Hub</text><text x="570" y="322" text-anchor="middle" fill="#a7cfc4" font-size="12">Monitor • Correlate • Predict • Decide</text></g>\n      <path d="M668 220 C755 165 832 142 910 136" stroke="url(#beamFlow)" stroke-width="5" fill="none"/><path d="M690 288 C770 288 830 288 900 288" stroke="url(#beamFlow)" stroke-width="5" fill="none"/><path d="M668 354 C755 410 832 436 910 444" stroke="url(#beamFlow)" stroke-width="5" fill="none"/><path d="M472 220 C390 165 330 324 252 326" stroke="url(#beamFlow)" stroke-width="4" fill="none" opacity=".72"/><path d="M472 354 C392 404 335 410 258 408" stroke="url(#beamFlow)" stroke-width="4" fill="none" opacity=".72"/>\n      <g class="pulseNode" filter="url(#softShadow)"><polygon points="920,104 988,144 988,224 920,264 852,224 852,144" fill="rgba(10,54,45,.88)" stroke="#67e8a5" stroke-opacity=".35"/><text x="920" y="178" class="nodeTitle">Safety</text><text x="920" y="201" class="nodeSub">Dam & operation risk</text></g>\n      <g class="pulseNode" filter="url(#softShadow)" style="animation-delay:.35s"><polygon points="920,248 988,288 988,368 920,408 852,368 852,288" fill="rgba(7,45,62,.90)" stroke="#7df9ff" stroke-opacity=".34"/><text x="920" y="322" class="nodeTitle">Asset</text><text x="920" y="345" class="nodeSub">Reliability & O&M</text></g>\n      <g class="pulseNode" filter="url(#softShadow)" style="animation-delay:.7s"><polygon points="920,392 988,432 988,512 920,552 852,512 852,432" fill="rgba(66,49,17,.80)" stroke="#ffd166" stroke-opacity=".42"/><text x="920" y="466" class="nodeTitle">Executive</text><text x="920" y="489" class="nodeSub">KPI & decision support</text></g>\n      <g class="pulseNode" filter="url(#softShadow)" style="animation-delay:1.05s"><polygon points="230,288 286,321 286,387 230,420 174,387 174,321" fill="rgba(8,54,45,.78)" stroke="#67e8a5" stroke-opacity=".30"/><text x="230" y="348" class="nodeTitle">Energy</text><text x="230" y="371" class="nodeSub">Generation optimization</text></g>\n      <g class="pulseNode" filter="url(#softShadow)" style="animation-delay:1.4s"><polygon points="230,374 286,407 286,473 230,506 174,473 174,407" fill="rgba(8,43,50,.80)" stroke="#5eead4" stroke-opacity=".30"/><text x="230" y="434" class="nodeTitle">ESG</text><text x="230" y="457" class="nodeSub">Environment reporting</text></g>\n      <g filter="url(#softShadow)"><rect x="338" y="456" width="400" height="78" rx="24" fill="rgba(13,47,39,.82)" stroke="#ffd166" stroke-opacity=".22"/><text x="538" y="489" text-anchor="middle" fill="#ffd166" font-size="13" font-weight="900" letter-spacing="1.2">BUSINESS OUTCOME</text><text x="538" y="515" text-anchor="middle" fill="#f2fff9" font-size="20" font-weight="900">Operational Excellence</text></g>\n      <path d="M570 419 L570 456" stroke="url(#beamFlow)" stroke-width="6" filter="url(#glowStrong)"/>\n      <g transform="translate(344 118)"><rect x="0" y="0" width="152" height="56" rx="16" fill="rgba(255,255,255,.045)" stroke="#5eead4" stroke-opacity=".14"/><text x="76" y="23" text-anchor="middle" fill="#a7cfc4" font-size="11" font-weight="800">VISION ACHIEVEMENT</text><text x="76" y="45" text-anchor="middle" fill="#b8ffd6" font-size="18" font-weight="900">98.6%</text></g>\n      <g transform="translate(654 118)"><rect x="0" y="0" width="152" height="56" rx="16" fill="rgba(255,255,255,.045)" stroke="#ffd166" stroke-opacity=".16"/><text x="76" y="23" text-anchor="middle" fill="#a7cfc4" font-size="11" font-weight="800">ESG READINESS</text><text x="76" y="45" text-anchor="middle" fill="#ffd166" font-size="18" font-weight="900">96.9%</text></g>\n    </svg></div>'

def roadmap_panel():
    items = [
        ("Phase 1 • Executive POC", "Dashboard command center, animated digital twin, simulated telemetry, executive narrative, value demonstration."),
        ("Phase 2 • Sensor Integration", "Connect dam, hydrology, turbine, electrical, water quality, and panel instrumentation through MQTT/Modbus/OPC-UA."),
        ("Phase 3 • AI Baseline", "Build local baseline, anomaly detection, predictive maintenance, dam safety index, hydrology and generation optimization."),
        ("Phase 4 • Enterprise Rollout", "Role-based operation center, report automation, mobile alert, audit trail, ESG dashboard, and management KPI."),
    ]
    st.markdown('<div class="timeline">', unsafe_allow_html=True)
    for h,b in items:
        st.markdown(f'<div class="timeline-item"><b>{h}</b><p>{b}</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)




def station_card(icon, name, location, status, params):
    is_weather = "weather" in name.lower()
    cls = "station-card weather-rain" if is_weather else "station-card"
    rain = '<div class="rain-layer"></div>' if is_weather else ''
    html = f'<div class="{cls}">{rain}<div class="station-icon">{icon}</div><div class="station-name">{name}</div><div class="station-meta">{location}</div><span class="risk-chip">{status}</span>'
    for k, v in params:
        html += f'<div class="station-param"><span>{k}</span><b>{v}</b></div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

def corr_status(score):
    if score >= 88:
        return "EXCELLENT", "Strong dependency detected across weather, reservoir, dam safety, turbine, and grid operation.", "#67e8a5"
    if score >= 75:
        return "MODERATE", "Correlation is usable but reduced. Review unstable inflow telemetry or sensor synchronization.", "#ffd166"
    return "WEAK", "Subsystem synchronization degraded. Inspection and telemetry validation recommended.", "#fb7185"

def dq_status(score):
    if score >= 98:
        return "EXCELLENT", "High-confidence telemetry. Suitable for predictive analytics and executive reporting.", "#67e8a5"
    if score >= 94:
        return "GOOD", "Telemetry is reliable with minor packet or timestamp deviation. Continue monitoring.", "#ffd166"
    return "WATCH", "Data confidence reduced. Validate communications, timestamp sync, and missing packet rate.", "#fb7185"

def subsystem_network_svg():
    corr = data['corr_score']
    corr_label, corr_text, corr_color = corr_status(corr)
    rain = data['rainfall']
    reservoir = data['reservoir_pct']
    dam = data['dam_health']
    vib = data['vib']
    freq = data['freq']
    pf = data['pf']
    ph = data['ph']
    turb = data['turbidity']
    pm25 = data['pm25']
    active_path = "Weather → Reservoir → Dam → Turbine → Grid" if rain >= 10 else "Reservoir → Dam → Turbine → Grid"
    rain_opacity = min(1, max(.45, rain/28))
    return f"""
<div class="panel subsystem-map-panel">
  <div class="subsys-title">Subsystem Command Centre Intelligence Map</div>
  <div class="subsys-subtitle">Live 2-second simulation: HOIP correlates field stations, civil instrumentation, turbine condition, and grid status into one operational story.</div>
  <div class="subsys-stage">
    <div class="flow-line l-weather-res" style="opacity:{rain_opacity:.2f};"><span></span></div>
    <div class="flow-line l-env-res"><span></span></div>
    <div class="flow-line l-res-dam"><span></span></div>
    <div class="flow-line l-dam-turb"><span></span></div>
    <div class="flow-line l-turb-grid"><span></span></div>
    <div class="flow-line l-wq-dam muted"><span></span></div>
    <div class="node n-weather"><b>RAIN</b><em></em></div>
    <div class="node-label lab-weather"><strong>Weather</strong><small>Rain {rain:.1f} mm/h</small></div>
    <div class="node n-env"><b>ENV</b><em></em></div>
    <div class="node-label lab-env"><strong>Air Quality</strong><small>PM2.5 {pm25:.1f}</small></div>
    <div class="node n-res"><b>WATER</b><em></em></div>
    <div class="node-label lab-res"><strong>Reservoir</strong><small>{reservoir:.1f}% storage</small></div>
    <div class="node n-wq"><b>WQ</b><em></em></div>
    <div class="node-label lab-wq"><strong>Water Quality</strong><small>pH {ph:.2f} • TURB {turb:.0f}</small></div>
    <div class="node dam-core"><i></i><b>DAM CORE</b><em></em></div>
    <div class="node-label lab-dam"><strong>Dam Safety</strong><small>{dam:.1f}% normal</small></div>
    <div class="node n-turb"><b>TURB</b><em></em></div>
    <div class="node-label lab-turb"><strong>Turbine</strong><small>VIB {vib:.2f} mm/s</small></div>
    <div class="node n-grid"><b>GRID</b><em></em></div>
    <div class="node-label lab-grid"><strong>Switchyard</strong><small>{freq:.2f} Hz • PF {pf:.3f}</small></div>
    <div class="active-path-card"><b>ACTIVE PATH</b><span>{active_path}</span></div>
    <div class="corr-card-mini"><b>Correlation Score</b><strong>{corr:.1f}%</strong><span style="color:{corr_color};">{corr_label}</span></div>
  </div>
</div>
"""

def correlation_flow_panel():
    flows = [
        ('Weather → Hydrology', 'Rainfall + upstream weather explain inflow trend, reservoir level rise, and spillway readiness.'),
        ('Weather + Reservoir → Dam Safety', 'Sustained rainfall is correlated with piezometer pressure, seepage, deformation, and civil watch status.'),
        ('Hydrology → Generation Optimization', 'Reservoir storage and inflow forecast determine safe dispatch, expected MW, and water-to-energy efficiency.'),
        ('Turbine + Electrical → Predictive O&M', 'Vibration, bearing temperature, load, PF, THD, transformer temperature become one maintenance-risk chain.'),
        ('Water Quality + Sedimentation → ESG & Operation', 'Turbidity, pH, DO, conductivity and sediment trend inform environmental compliance and reservoir capacity.'),
        ('Air Quality + ESG → Community & Compliance', 'PM2.5, PM10, NO₂, CO and weather context support environmental reporting and impact monitoring.'),
    ]
    for h, b in flows:
        st.markdown(f'<div class="corr-line"><b>{h}</b><p>{b}</p></div>', unsafe_allow_html=True)


def subsystem_command_component(refresh_sec=2):
    html = r'''<!doctype html><html><head><meta charset="UTF-8"><style>
*{box-sizing:border-box}body{margin:0;font-family:Inter,Arial,sans-serif;color:#eef7ff;background:transparent;overflow:hidden}.wrap{padding:0 0 14px}.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-bottom:18px}.kpi{border:1px solid rgba(94,234,212,.22);background:linear-gradient(160deg,rgba(7,57,45,.80),rgba(4,24,30,.70));border-radius:22px;padding:18px 20px;min-height:138px;box-shadow:inset 0 1px 0 rgba(255,255,255,.04),0 18px 42px rgba(0,0,0,.22);position:relative;overflow:hidden}.kpi:before{content:"";position:absolute;right:-28px;top:-30px;width:115px;height:115px;border-radius:50%;background:radial-gradient(circle,rgba(52,211,153,.25),transparent 68%)}.kl{color:#a7cfc4;font-size:12px;font-weight:900;text-transform:uppercase;letter-spacing:.9px;position:relative;z-index:1}.kv{font-size:33px;font-weight:900;margin-top:22px;letter-spacing:-.9px;position:relative;z-index:1}.ku{font-size:17px;color:#c8e8e0;margin-left:4px;font-weight:800}.kn{color:#b4d8cf;font-size:12px;margin-top:16px;position:relative;z-index:1}.spark{height:2px;width:100%;margin-top:13px;border-radius:99px;background:linear-gradient(90deg,rgba(94,234,212,.08),rgba(94,234,212,.84),rgba(52,211,153,.08));background-size:220% 100%;animation:spark 2s linear infinite}@keyframes spark{from{background-position:0 0}to{background-position:220% 0}}
.grid{display:grid;grid-template-columns:1.78fr 1fr;gap:18px;align-items:start}.panel{border:1px solid rgba(94,234,212,.22);background:linear-gradient(160deg,rgba(7,54,45,.74),rgba(3,22,28,.70));border-radius:26px;box-shadow:0 22px 60px rgba(0,0,0,.24);overflow:hidden}.map{height:640px;position:relative;background:linear-gradient(160deg,rgba(4,38,33,.84),rgba(3,16,26,.78))}.map:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 18% 18%,rgba(94,234,212,.10),transparent 28%),radial-gradient(circle at 72% 55%,rgba(255,209,102,.08),transparent 30%),repeating-linear-gradient(45deg,rgba(94,234,212,.045) 0 1px,transparent 1px 58px),repeating-linear-gradient(-45deg,rgba(94,234,212,.035) 0 1px,transparent 1px 58px)}.map:after{content:"";position:absolute;left:0;right:0;bottom:0;height:160px;background:linear-gradient(160deg,transparent,rgba(7,49,40,.35));clip-path:polygon(0 70%,20% 58%,43% 64%,60% 48%,78% 66%,100% 42%,100% 100%,0 100%)}.title{position:absolute;left:36px;top:30px;font-size:24px;font-weight:900;z-index:5}.sub{position:absolute;left:36px;top:67px;font-size:12px;color:#a7cfc4;z-index:5;max-width:860px}.stage{position:absolute;inset:0;z-index:3}.node{position:absolute;width:118px;height:118px;border-radius:50%;background:radial-gradient(circle at 42% 26%,#154b69 0%,#0a253d 58%,#071726 100%);border:1px solid rgba(94,234,212,.42);box-shadow:0 20px 45px rgba(0,0,0,.35),0 0 24px rgba(94,234,212,.18);display:flex;align-items:center;justify-content:center;animation:nodeFloat 3.1s ease-in-out infinite}.node b{font-size:11px;font-weight:900;color:#b8ffd6;text-shadow:0 0 10px rgba(184,255,214,.75);letter-spacing:.6px}.node em{position:absolute;left:50%;top:55%;width:16px;height:16px;margin-left:-8px;margin-top:-8px;border-radius:50%;background:#67e8a5;box-shadow:0 0 18px rgba(103,232,165,.92)}.dam{width:158px;height:158px;background:radial-gradient(circle at 44% 30%,#5a411a 0%,#12354a 56%,#061523 100%);border:2px solid rgba(255,209,102,.58);box-shadow:0 22px 62px rgba(0,0,0,.44),0 0 34px rgba(255,209,102,.20);animation:damPulse 2.5s ease-in-out infinite}.dam i{position:absolute;inset:-18px;border:2px solid rgba(255,209,102,.32);border-radius:50%;animation:ring 2.8s ease-out infinite}.dam b{color:#ffd166;font-size:12px}.dam em{background:#ffd166;box-shadow:0 0 18px rgba(255,209,102,.95)}.label{position:absolute;min-width:128px;padding:8px 11px;border-radius:13px;background:rgba(2,18,26,.84);border:1px solid rgba(94,234,212,.24);box-shadow:0 12px 22px rgba(0,0,0,.36);text-align:center;backdrop-filter:blur(8px);z-index:5}.label strong{display:block;color:#eef8ff;font-size:13px;font-weight:900;line-height:1.1}.label small{display:block;color:#b6d8d0;font-size:11px;margin-top:5px;white-space:nowrap}.nw{left:85px;top:116px}.lw{left:78px;top:244px}.ne{left:365px;top:116px}.le{left:358px;top:244px}.nr{left:655px;top:128px}.lr{left:648px;top:258px}.nq{left:92px;top:366px}.lq{left:68px;top:494px}.dam{left:372px;top:338px}.ld{left:382px;top:512px}.nt{left:655px;top:376px}.lt{left:648px;top:504px}.ng{left:835px;top:158px}.lg{left:812px;top:288px}.flow{position:absolute;height:4px;border-radius:99px;background:linear-gradient(90deg,rgba(94,234,212,.12),rgba(125,249,255,.88),rgba(103,232,165,.88),rgba(255,209,102,.20));box-shadow:0 0 16px rgba(94,234,212,.36);overflow:hidden;transform-origin:left center;z-index:2}.flow:before{content:"";position:absolute;inset:1px;background:repeating-linear-gradient(90deg,transparent 0 18px,rgba(255,255,255,.75) 18px 31px,transparent 31px 48px);animation:dash 1.6s linear infinite}.flow span{position:absolute;top:50%;left:-10px;width:10px;height:10px;margin-top:-5px;border-radius:50%;background:#7df9ff;box-shadow:0 0 14px rgba(125,249,255,.95);animation:packet 2.4s linear infinite}.f1{left:200px;top:175px;width:190px;transform:rotate(-7deg)}.f2{left:480px;top:176px;width:198px;transform:rotate(4deg)}.f3{left:558px;top:303px;width:208px;transform:rotate(132deg)}.f4{left:515px;top:438px;width:160px;transform:rotate(4deg)}.f5{left:754px;top:370px;width:145px;transform:rotate(-51deg)}.f6{left:210px;top:452px;width:170px;transform:rotate(5deg);opacity:.65}.card,.mini{position:absolute;border-radius:18px;background:rgba(8,55,45,.86);border:1px solid rgba(103,232,165,.26);box-shadow:0 15px 35px rgba(0,0,0,.28);padding:13px 16px;backdrop-filter:blur(8px);z-index:7}.card{left:34px;bottom:30px;width:382px}.mini{right:32px;bottom:30px;width:235px}.card b,.mini b{display:block;color:#8fffe0;font-size:11px;font-weight:900;letter-spacing:1px}.card span{display:block;color:#eef8ff;font-size:13px;font-weight:800;margin-top:7px}.mini strong{display:inline-block;color:#eef8ff;font-size:28px;font-weight:900;margin-top:7px;margin-right:10px}.mini span{font-size:12px;font-weight:900;letter-spacing:.8px;color:#67e8a5}@keyframes nodeFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}@keyframes damPulse{0%,100%{filter:drop-shadow(0 0 7px rgba(255,209,102,.45))}50%{filter:drop-shadow(0 0 24px rgba(255,209,102,.95))}}@keyframes ring{0%{transform:scale(.88);opacity:.55}100%{transform:scale(1.35);opacity:0}}@keyframes dash{to{transform:translateX(48px)}}@keyframes packet{from{left:-12px}to{left:100%}}
.side{min-height:640px;padding:18px}.pt{display:flex;justify-content:space-between;gap:12px;align-items:center;margin-bottom:14px}.pt h3{margin:0;font-size:18px}.pt span{color:#a7cfc4;font-size:12px}.box{border:1px solid rgba(94,234,212,.24);background:linear-gradient(145deg,rgba(52,211,153,.12),rgba(8,21,38,.45));border-radius:22px;padding:16px;margin-bottom:12px}.bt{font-size:13px;color:#7fffd4;font-weight:900;text-transform:uppercase;letter-spacing:.8px}.txt{font-size:14px;color:#e8f7ff;line-height:1.55;margin-top:8px}.big{font-size:34px;font-weight:900;color:#eef8ff}.stat{color:#67e8a5;font-size:13px;font-weight:900;letter-spacing:1px}.mr{display:grid;grid-template-columns:1fr auto;gap:8px;border-bottom:1px solid rgba(94,234,212,.10);padding:11px 0}.mn{color:#c7d9e9;font-size:13px}.mv{font-size:13px;font-weight:900;color:#fff}.bottom{margin-top:18px;padding:18px}.bg{display:grid;grid-template-columns:1.05fr 1fr;gap:24px}.bar{margin:12px 0}.bh{display:flex;justify-content:space-between;color:#cfeee6;font-size:12px;margin-bottom:6px}.bb{height:11px;border-radius:999px;background:rgba(255,255,255,.08);overflow:hidden}.bf{height:100%;border-radius:999px;background:linear-gradient(90deg,#34d399,#5eead4);transition:width .6s ease}.heat{background:linear-gradient(90deg,#134e4a,#2dd4bf,#ffd166);box-shadow:0 0 14px rgba(45,212,191,.28)}
</style></head><body><div class="wrap"><div class="kpis"><div class="kpi"><div class="kl">CONNECTED SUBSYSTEMS</div><div class="kv">10<span class="ku"> nodes</span></div><div class="kn">Station + asset instrumentation</div><div class="spark"></div></div><div class="kpi"><div class="kl">CORRELATION SCORE</div><div class="kv"><span id="k_corr">91.8</span><span class="ku">%</span></div><div class="kn"><span id="k_corr_note">EXCELLENT</span> • local live update</div><div class="spark"></div></div><div class="kpi"><div class="kl">DATA QUALITY</div><div class="kv"><span id="k_dq">99.3</span><span class="ku">%</span></div><div class="kn"><span id="k_dq_note">EXCELLENT</span> • predictive-ready</div><div class="spark"></div></div><div class="kpi"><div class="kl">ACTIVE ADVISORY</div><div class="kv">4<span class="ku"> items</span></div><div class="kn">No critical alarm</div><div class="spark"></div></div></div><div class="grid"><div class="panel map"><div class="title">Subsystem Command Centre Intelligence Map</div><div class="sub">Local 2-second simulation: HOIP correlates field stations, civil instrumentation, turbine condition, and grid status into one operational story.</div><div class="stage"><div class="flow f1"><span></span></div><div class="flow f2"><span></span></div><div class="flow f3"><span></span></div><div class="flow f4"><span></span></div><div class="flow f5"><span></span></div><div class="flow f6"><span></span></div><div class="node nw"><b>RAIN</b><em></em></div><div class="label lw"><strong>Weather</strong><small>Rain <span id="rain">14.2</span> mm/h</small></div><div class="node ne"><b>ENV</b><em></em></div><div class="label le"><strong>Air Quality</strong><small>PM2.5 <span id="pm25">18.0</span></small></div><div class="node nr"><b>WATER</b><em></em></div><div class="label lr"><strong>Reservoir</strong><small><span id="reservoir">82.4</span>% storage</small></div><div class="node nq"><b>WQ</b><em></em></div><div class="label lq"><strong>Water Quality</strong><small>pH <span id="ph">7.18</span> • TURB <span id="turb">22</span></small></div><div class="node dam"><i></i><b>DAM CORE</b><em></em></div><div class="label ld"><strong>Dam Safety</strong><small><span id="dam">98.2</span>% normal</small></div><div class="node nt"><b>TURB</b><em></em></div><div class="label lt"><strong>Turbine</strong><small>VIB <span id="vib">2.10</span> mm/s</small></div><div class="node ng"><b>GRID</b><em></em></div><div class="label lg"><strong>Switchyard</strong><small><span id="freq">50.01</span> Hz • PF <span id="pf">0.987</span></small></div><div class="card"><b>ACTIVE PATH</b><span id="activePath">Weather → Reservoir → Dam → Turbine → Grid</span></div><div class="mini"><b>Correlation Score</b><strong><span id="mini_corr">91.8</span>%</strong><span id="mini_corr_label">EXCELLENT</span></div></div></div><div class="panel side"><div class="pt"><h3>Live Intelligence Interpretation</h3><span>local update, no page reload</span></div><div class="box"><div class="bt">Correlation Intelligence</div><div class="txt"><div style="display:flex;align-items:baseline;gap:12px;margin-bottom:8px"><span class="big"><span id="side_corr">91.8</span>%</span><span class="stat" id="side_corr_label">EXCELLENT</span></div><span id="corrText">Strong dependency detected across weather, reservoir, dam safety, turbine, and grid operation.</span><br><br><b>Active dependency:</b> <span id="sidePath">Weather → Reservoir → Dam → Turbine → Grid.</span></div></div><div class="box"><div class="bt">Data Quality Intelligence</div><div class="txt"><div style="display:flex;align-items:baseline;gap:12px;margin-bottom:8px"><span class="big"><span id="side_dq">99.3</span>%</span><span class="stat" id="side_dq_label">EXCELLENT</span></div><span id="dqText">High-confidence telemetry. Suitable for predictive analytics and executive reporting.</span></div></div><div class="mr"><div class="mn">Telemetry Completeness</div><div class="mv"><span id="comp">99.7</span>%</div></div><div class="mr"><div class="mn">Timestamp Integrity</div><div class="mv"><span id="ts">99.5</span>%</div></div><div class="mr"><div class="mn">Communication Health</div><div class="mv"><span id="comm">99.2</span>%</div></div><div class="mr"><div class="mn">Missing Packet</div><div class="mv"><span id="miss">0.70</span>%</div></div><div class="box" style="margin-top:14px"><div class="bt">Current Operational Story</div><div class="txt" id="story">Rainfall acts as the upstream driver for reservoir behaviour. Reservoir level remains inside the operating band, dam safety indicators are normal, turbine vibration is stable, and grid export quality remains within acceptable range.</div></div></div></div><div class="panel bottom"><div class="pt"><h3>Subsystem Health & Correlation Heatmap</h3><span>Live station quality and cross-system reasoning</span></div><div class="bg"><div id="healthBars"></div><div id="heatBars"></div></div></div></div><script>
const refreshMs=Math.max(1000,__REFRESH__*1000),$=id=>document.getElementById(id);function f(b,a,fr,p=0){return b+a*Math.sin((Date.now()/1000+p)/fr)}function clamp(v,a,b){return Math.max(a,Math.min(b,v))}function sc(v){return v>=88?['EXCELLENT','Strong dependency detected across weather, reservoir, dam safety, turbine, and grid operation.']:v>=74?['MODERATE','Correlation is stable, but some telemetry streams need attention before advanced prediction.']:['WEAK','Subsystem relationship is degraded. Verify telemetry continuity and station synchronization.']}function sd(v){return v>=97?['EXCELLENT','High-confidence telemetry. Suitable for predictive analytics and executive reporting.']:v>=92?['GOOD','Telemetry is usable, with minor gaps that should be monitored.']:['REVIEW','Data integrity requires investigation before operational recommendation.']}function tx(id,val){let e=$(id);if(e)e.textContent=val}function bar(n,v,c=''){return `<div class="bar"><div class="bh"><span>${n}</span><b>${v.toFixed(1)}%</b></div><div class="bb"><div class="bf ${c}" style="width:${v.toFixed(1)}%"></div></div></div>`}function update(){let now=Date.now()/1000,corr=clamp(f(91.7,1.15,7)+Math.sin(now/3)*.22,88.6,94.4),dq=clamp(f(99.25,.23,9,2),98.6,99.7),rain=clamp(f(14.1,4.4,6,.5),6.5,22.8),res=clamp(f(82.5,1.3,10,1),79.8,85.2),dam=clamp(f(98.2,.22,8,2),97.6,98.8),vib=clamp(f(2.10,.16,5,.3),1.76,2.44),freq=clamp(f(50.01,.025,4,.7),49.96,50.06),pf=clamp(f(.987,.004,5,1.4),.978,.992),ph=clamp(f(7.18,.10,6,2.1),6.95,7.35),turb=clamp(f(22,4.6,5,.9),13,31),pm25=clamp(f(18,5.2,6,1.1),8,28),cs=sc(corr),ds=sd(dq);['k_corr','mini_corr','side_corr'].forEach(id=>tx(id,corr.toFixed(1)));['k_corr_note','mini_corr_label','side_corr_label'].forEach(id=>tx(id,cs[0]));tx('corrText',cs[1]);['k_dq','side_dq'].forEach(id=>tx(id,dq.toFixed(1)));['k_dq_note','side_dq_label'].forEach(id=>tx(id,ds[0]));tx('dqText',ds[1]);tx('rain',rain.toFixed(1));tx('reservoir',res.toFixed(1));tx('dam',dam.toFixed(1));tx('vib',vib.toFixed(2));tx('freq',freq.toFixed(2));tx('pf',pf.toFixed(3));tx('ph',ph.toFixed(2));tx('turb',turb.toFixed(0));tx('pm25',pm25.toFixed(1));tx('comp',clamp(dq+.42,98.8,99.9).toFixed(1));tx('ts',clamp(dq+.18,98.6,99.8).toFixed(1));tx('comm',clamp(dq-.12,98.2,99.6).toFixed(1));tx('miss',clamp(100-dq+.04,.08,.88).toFixed(2));let path=rain>11?'Weather → Reservoir → Dam → Turbine → Grid':'Reservoir → Dam → Turbine → Grid';tx('activePath',path);tx('sidePath',path+'.');tx('story',`Rainfall is currently ${rain.toFixed(1)} mm/h and acts as the upstream driver for reservoir behaviour. Reservoir level remains at ${res.toFixed(1)}% storage, dam safety is ${dam.toFixed(1)}%, turbine vibration is ${vib.toFixed(2)} mm/s, and grid export quality remains within acceptable range.`);let health=[['Weather Station',97.4+Math.sin(now/5)*.7],['Air Quality Station',94.8+Math.sin(now/6)*.8],['Water Quality Station',95.6+Math.sin(now/6.5)*.7],['Dam Instrumentation',dam],['Turbine Monitoring',96.8+Math.sin(now/7)*.6],['Electrical & Switchyard',97.1+Math.sin(now/8)*.5]];$('healthBars').innerHTML=health.map(x=>bar(x[0],x[1])).join('');let heat=[['Weather → Reservoir',Math.min(99,corr+3.8)],['Reservoir → Dam',Math.min(99,corr+2.2)],['Dam → Turbine',Math.max(75,corr-1.8)],['Turbine → Grid',Math.max(72,corr-.6)],['Water Quality → ESG',Math.max(70,corr-4.5)],['Air Quality → ESG',Math.max(68,corr-6.2)]];$('heatBars').innerHTML=heat.map(x=>bar(x[0],x[1],'heat')).join('')}update();setInterval(update,refreshMs);</script></body></html>'''
    return html.replace('__REFRESH__', str(int(refresh_sec)))


def operational_correlation_component():
    rain = data['rainfall']
    inflow = data['inflow']
    outflow = data['outflow']
    net = inflow - outflow
    storage = data['reservoir_pct']
    level = data['reservoir_level']
    pz = data['piezometer']
    seep = data['seepage']
    gen = data['generation']
    turb = data['turbidity']
    pm25 = data['pm25']
    corr = data['corr_score']
    rain_int = "MEDIUM" if rain < 18 else "HIGH"
    flood = "LOW" if rain < 18 and net < 180 else "WATCH"
    spillway = "CLOSED" if storage < 86 else "STANDBY"
    dam_risk = "NORMAL" if pz < 148 and seep < 22 else "WATCH"
    mw_delta = max(0, min(42, net / 8))
    sediment = "MODERATE" if turb > 24 else "LOW"
    html = """<!doctype html><html><head><meta charset='UTF-8'><style>
*{box-sizing:border-box}body{margin:0;background:transparent;color:#eef7ff;font-family:Inter,Arial,sans-serif;overflow:hidden}.wrap{padding:0}.hero{border:1px solid rgba(94,234,212,.22);background:linear-gradient(160deg,rgba(5,44,38,.78),rgba(3,16,26,.72));border-radius:26px;padding:20px;box-shadow:0 20px 52px rgba(0,0,0,.28);height:850px;position:relative;overflow:hidden}.hero:before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 18% 18%,rgba(94,234,212,.14),transparent 30%),radial-gradient(circle at 70% 40%,rgba(255,209,102,.09),transparent 28%),repeating-linear-gradient(45deg,rgba(94,234,212,.035) 0 1px,transparent 1px 58px);pointer-events:none}.title{position:relative;z-index:2;display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px}.title h2{margin:0;font-size:27px;letter-spacing:-.6px}.title p{margin:7px 0 0;color:#a7cfc4;font-size:13px}.badge{border:1px solid rgba(103,232,165,.34);background:rgba(16,185,129,.11);border-radius:999px;padding:10px 14px;color:#b8ffd6;font-weight:900;font-size:12px}.grid{position:relative;z-index:2;display:grid;grid-template-columns:1.22fr .86fr;gap:18px}.left,.right{min-height:735px}.chain{height:735px;border:1px solid rgba(94,234,212,.16);background:linear-gradient(160deg,rgba(3,25,33,.63),rgba(5,42,35,.55));border-radius:24px;padding:18px;position:relative;overflow:hidden}.river{position:absolute;left:32px;right:32px;top:76px;height:5px;border-radius:999px;background:linear-gradient(90deg,rgba(94,234,212,.18),rgba(94,234,212,.85),rgba(255,209,102,.72),rgba(94,234,212,.25));background-size:220% 100%;animation:flow 2.4s linear infinite;box-shadow:0 0 20px rgba(94,234,212,.35)}@keyframes flow{from{background-position:0 0}to{background-position:220% 0}}.stage{position:relative;margin:34px 0 0;display:grid;grid-template-columns:140px 1fr 185px;gap:12px;align-items:center}.node{border:1px solid rgba(94,234,212,.28);background:radial-gradient(circle at 30% 20%,rgba(94,234,212,.20),rgba(7,31,48,.88));border-radius:20px;padding:13px;min-height:74px;box-shadow:0 15px 28px rgba(0,0,0,.24)}.node b{font-size:14px}.node small{display:block;color:#a9c9c1;margin-top:5px;line-height:1.35}.effect{border:1px solid rgba(255,209,102,.22);background:linear-gradient(145deg,rgba(255,209,102,.09),rgba(94,234,212,.06));border-radius:18px;padding:12px;font-size:12px;line-height:1.45;color:#e7f9ff}.impact{border:1px solid rgba(103,232,165,.24);background:rgba(103,232,165,.08);border-radius:18px;padding:12px;text-align:right}.impact strong{display:block;font-size:20px;color:#f2fff9;letter-spacing:-.5px}.impact span{font-size:11px;color:#b8ffd6;font-weight:900;text-transform:uppercase}.arrow{height:20px;margin-left:68px;border-left:2px dashed rgba(94,234,212,.32)}.pulse-dot{display:inline-block;width:9px;height:9px;border-radius:50%;background:#67e8a5;box-shadow:0 0 14px rgba(103,232,165,.9);margin-right:7px}.right{display:grid;grid-template-rows:auto auto auto 1fr;gap:12px}.panel{border:1px solid rgba(94,234,212,.19);background:linear-gradient(160deg,rgba(7,54,45,.70),rgba(3,21,31,.64));border-radius:23px;padding:16px;box-shadow:0 18px 36px rgba(0,0,0,.22)}.pt{display:flex;justify-content:space-between;margin-bottom:10px;color:#a7cfc4;font-size:12px}.pt b{color:#7fffd4;text-transform:uppercase;letter-spacing:.8px}.story{font-size:15px;line-height:1.55;color:#f1fbff}.story b{color:#b8ffd6}.mrow{display:grid;grid-template-columns:1fr auto;gap:12px;padding:9px 0;border-bottom:1px solid rgba(94,234,212,.10);font-size:13px}.mrow:last-child{border-bottom:0}.mrow span{color:#b9d0dd}.mrow b{color:#fff}.matrix{display:grid;gap:8px}.bar{display:grid;grid-template-columns:120px 1fr 45px;gap:9px;align-items:center;font-size:12px}.track{height:10px;border-radius:99px;background:rgba(255,255,255,.09);overflow:hidden}.fill{height:100%;border-radius:99px;background:linear-gradient(90deg,#5eead4,#67e8a5,#ffd166);box-shadow:0 0 14px rgba(94,234,212,.35)}.decision{border-color:rgba(255,209,102,.32);background:linear-gradient(145deg,rgba(255,209,102,.12),rgba(4,27,35,.64))}.decision .action{font-size:25px;font-weight:900;color:#ffd166;letter-spacing:-.5px}.chips{margin-top:10px}.chip{display:inline-flex;margin:4px 5px 0 0;padding:7px 9px;border-radius:999px;border:1px solid rgba(94,234,212,.22);background:rgba(255,255,255,.05);font-size:11px;color:#d4fff2}.subnote{font-size:11px;color:#a7cfc4;margin-top:8px;line-height:1.4}
</style></head><body><div class='wrap'><div class='hero'><div class='title'><div><h2>Operational Correlation & Impact Engine</h2><p>What changed upstream, what it affects inside the dam, and what decision should follow.</p></div><div class='badge'>CORRELATION SCORE __CORR__% • ACTIVE</div></div><div class='grid'><div class='left'><div class='chain'><div class='river'></div>
<div class='stage'><div class='node'><b><span class='pulse-dot'></span>Weather Driver</b><small>Rainfall intensity __RAIN__ mm/h • __RAININT__</small></div><div class='effect'>Rainfall and catchment condition become the upstream driver for inflow shape and reservoir rise.</div><div class='impact'><strong>+18%</strong><span>inflow pressure</span></div></div><div class='arrow'></div>
<div class='stage'><div class='node'><b>Hydrology Response</b><small>Inflow __INFLOW__ m³/s • net balance __NET__ m³/s</small></div><div class='effect'>Upstream hydrograph enters rising limb. Forecast peak is expected in 4–6 hours if rainfall persists.</div><div class='impact'><strong>__FLOOD__</strong><span>flood routing risk</span></div></div><div class='arrow'></div>
<div class='stage'><div class='node'><b>Reservoir Operation</b><small>Storage __STORAGE__% • EL __LEVEL__ m</small></div><div class='effect'>Actual storage remains inside rule curve. Release can stay generation-controlled without opening spillway.</div><div class='impact'><strong>__SPILLWAY__</strong><span>spillway status</span></div></div><div class='arrow'></div>
<div class='stage'><div class='node'><b>Dam Safety Chain</b><small>Pore pressure __PZ__ kPa • seepage __SEEP__ L/min</small></div><div class='effect'>Pore pressure responds to rainfall, but seepage and deformation remain inside baseline. No structural distress pattern.</div><div class='impact'><strong>__DAMRISK__</strong><span>civil risk</span></div></div><div class='arrow'></div>
<div class='stage'><div class='node'><b>Powerhouse Dispatch</b><small>Generation __GEN__ MW • water-to-energy opportunity</small></div><div class='effect'>Positive net inflow supports stable dispatch. Potential additional generation margin is available without hydraulic stress.</div><div class='impact'><strong>+__MWDELTA__ MW</strong><span>dispatch potential</span></div></div><div class='arrow'></div>
<div class='stage'><div class='node'><b>Environmental Link</b><small>Turbidity __TURB__ NTU • PM2.5 __PM25__ µg/m³</small></div><div class='effect'>Water quality and sediment trend are watched for ESG reporting, dead-storage impact, and downstream irrigation suitability.</div><div class='impact'><strong>__SEDIMENT__</strong><span>sediment watch</span></div></div>
</div></div><div class='right'>
<div class='panel'><div class='pt'><b>Current Operational Story</b><span>cause → effect → decision</span></div><div class='story'><b>Rainfall is driving inflow upward</b>, but reservoir storage remains inside the planned operating band. Dam safety indicators stay normal, so generation can continue under normal dispatch while upstream hydrograph is watched.</div></div>
<div class='panel'><div class='pt'><b>Impact Matrix</b><span>strength</span></div><div class='matrix'><div class='bar'><span>Weather → Hydrology</span><div class='track'><div class='fill' style='width:92%'></div></div><b>92%</b></div><div class='bar'><span>Hydrology → Reservoir</span><div class='track'><div class='fill' style='width:88%'></div></div><b>88%</b></div><div class='bar'><span>Reservoir → Dam</span><div class='track'><div class='fill' style='width:81%'></div></div><b>81%</b></div><div class='bar'><span>Dam → Dispatch</span><div class='track'><div class='fill' style='width:74%'></div></div><b>74%</b></div><div class='bar'><span>Sediment → ESG</span><div class='track'><div class='fill' style='width:69%'></div></div><b>69%</b></div></div></div>
<div class='panel'><div class='pt'><b>Risk Propagation</b><span>active chain</span></div><div class='mrow'><span>Heavy rainfall → high inflow</span><b>ACTIVE</b></div><div class='mrow'><span>High inflow → reservoir rise</span><b>WATCH</b></div><div class='mrow'><span>Reservoir rise → pore pressure</span><b>NORMAL</b></div><div class='mrow'><span>Seepage + deformation coupling</span><b>NOT DETECTED</b></div><div class='mrow'><span>Turbidity → dead storage sediment</span><b>__SEDIMENT__</b></div></div>
<div class='panel decision'><div class='pt'><b>Recommended Decision</b><span>operator action</span></div><div class='action'>NORMAL DISPATCH</div><div class='subnote'>Keep spillway closed, maintain turbine release, watch upstream hydrograph, and review reservoir operation if inflow peak exceeds forecast or pore pressure couples with seepage rise.</div><div class='chips'><span class='chip'>Spillway: __SPILLWAY__</span><span class='chip'>Dam Risk: __DAMRISK__</span><span class='chip'>Flood Routing: __FLOOD__</span><span class='chip'>Next Review: 2 hours</span></div></div>
</div></div></div></div></body></html>"""
    repl = {
        '__RAIN__': f"{rain:.1f}", '__RAININT__': rain_int, '__INFLOW__': f"{inflow:.0f}", '__NET__': f"{net:.0f}",
        '__STORAGE__': f"{storage:.1f}", '__LEVEL__': f"{level:.2f}", '__PZ__': f"{pz:.1f}", '__SEEP__': f"{seep:.1f}",
        '__GEN__': f"{gen:.0f}", '__TURB__': f"{turb:.1f}", '__PM25__': f"{pm25:.1f}", '__CORR__': f"{corr:.1f}",
        '__FLOOD__': flood, '__SPILLWAY__': spillway, '__DAMRISK__': dam_risk, '__MWDELTA__': f"{mw_delta:.0f}", '__SEDIMENT__': sediment
    }
    for k,v in repl.items(): html = html.replace(k, v)
    return html

st.sidebar.markdown(f'''<div style="padding:8px 0 18px 0;"><img src="data:image/png;base64,{KHN_LOGO_B64}" style="width:190px;max-width:100%;filter:drop-shadow(0 10px 22px rgba(0,0,0,.35));"></div>''', unsafe_allow_html=True)
st.sidebar.markdown("## HOIP")
st.sidebar.caption("Hydropower Operational Intelligence Platform")
page = st.sidebar.radio("Navigation", [
    "🏠 Executive Command Center",
    "🎯 Vision & Architecture",
    "🕸️ Subsystem Command Center",
    "🗺️ Subsystem Coverage Map",
    "🌦️ Weather Station",
    "🌫️ Air Quality Station",
    "💧 Water Quality Station",
    "🏛️ Dam Intelligence",
    "🌊 Reservoir & Hydrology",
    "🌀 Powerhouse & Turbine",
    "⚡ Electrical & Switchyard",
    "🔗 Correlation Intelligence",
    "🤖 AI Recommendation Center",
    "🛠️ Predictive O&M Value",
    "📊 ESG & Reporting",
    "🚀 Implementation Roadmap"
], label_visibility="collapsed")
st.sidebar.markdown("---")
live_mode = st.sidebar.toggle("Simulated Live Feed", value=True)
refresh_sec = st.sidebar.slider("Refresh interval", 1, 5, 2)
st.sidebar.markdown("### Client")
st.sidebar.markdown("**PT Kayan Hydropower Nusantara**")
st.sidebar.caption("Enterprise demonstration environment")


def _render_live_body():
    topbar()

    if page == "🏠 Executive Command Center":
        ai_insight_banner()
        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("Overall Plant Health", f"{data['plant_health']:.1f}", "%", "All critical systems operating normally")
        with c2: kpi("Generation Output", f"{data['generation']:.0f}", "MW", "3 units online • grid export stable")
        with c3: kpi("Reservoir Storage", f"{data['reservoir_pct']:.1f}", "%", f"EL {data['reservoir_level']:.2f} m • normal zone")
        with c4: kpi("Energy Today", f"{data['energy_today']:.2f}", "GWh", "Above daily operating baseline")
        left, right = st.columns([2.35, 1])
        with left:
            st.markdown(digital_dam_svg(), unsafe_allow_html=True)
        with right:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("AI Operational Brief", "Decision Support")
            st.markdown(f'''
            <div class="ai-box"><div class="ai-title">Current Recommendation</div><div class="ai-text">
            Reservoir remains within normal operating band. Forecasted inflow is positive and generation output is stable.
            Maintain current Unit #1–#3 dispatch. No spillway intervention required in the next operating window.</div></div>
            <div class="ai-box"><div class="ai-title">Early Signal</div><div class="ai-text">
            Piezometer PZ-07 shows a mild upward trend of {data['piezometer']-139:.1f} kPa against baseline.
            Risk remains low, but monitoring intensity should increase if rainfall persists.</div></div>
            ''', unsafe_allow_html=True)
            metric("Dam Safety Index", f"{data['dam_health']:.1f}%")
            metric("Turbine Health", f"{data['turbine_health']:.1f}%")
            metric("Electrical Health", f"{data['electrical_health']:.1f}%")
            metric("Switchyard Health", f"{data['switchyard_health']:.1f}%")
            metric("Maintenance Risk", f"{data['maintenance_risk']:.1f}%")
            metric("Active Alarm", "0 Critical / 2 Advisory")
            st.markdown('</div>', unsafe_allow_html=True)

        a,b,c = st.columns(3)
        with a:
            st.markdown(f'''
            <div class="panel exec-panel filled-panel">
              <div class="panel-title"><h3>🟢 System Health Matrix</h3><span>Live • Updated <span class="hoip-updated-time">{datetime.now().strftime('%H:%M:%S')}</span></span></div>
              <div class="mini-summary-grid">
                <div class="mini-summary"><div class="mini-icon">🏛️</div><b>{live_number_html(data['dam_health'])}%</b><span>Dam Civil</span></div>
                <div class="mini-summary"><div class="mini-icon">🌊</div><b>{live_number_html(96.4 + math.sin(t/21)*.8)}%</b><span>Hydrology</span></div>
                <div class="mini-summary"><div class="mini-icon">⚡</div><b>{live_number_html(data['electrical_health'])}%</b><span>Electrical</span></div>
              </div>
              <div class="health-list">
                <div class="health-row"><span>🏛️ Dam & Civil Structure</span><b>{live_number_html(data['dam_health'])}%</b><i><em style="width:{data['dam_health']:.1f}%"></em></i></div>
                <div class="health-row"><span>🌧️ Weather & Hydrology</span><b>{live_number_html(96.4 + math.sin(t/21)*.8)}%</b><i><em style="width:{96.4 + math.sin(t/21)*.8:.1f}%"></em></i></div>
                <div class="health-row"><span>💧 Water Quality</span><b>{live_number_html(95.6 + math.sin(t/18)*.7)}%</b><i><em style="width:{95.6 + math.sin(t/18)*.7:.1f}%"></em></i></div>
                <div class="health-row"><span>🌫️ Air Quality</span><b>{live_number_html(94.8 + math.sin(t/20)*.8)}%</b><i><em style="width:{94.8 + math.sin(t/20)*.8:.1f}%"></em></i></div>
                <div class="health-row"><span>⚙️ Turbine Generator</span><b>{live_number_html(data['turbine_health'])}%</b><i><em style="width:{data['turbine_health']:.1f}%"></em></i></div>
                <div class="health-row"><span>⚡ Electrical System</span><b>{live_number_html(data['electrical_health'])}%</b><i><em style="width:{data['electrical_health']:.1f}%"></em></i></div>
                <div class="health-row"><span>🔌 Switchyard</span><b>{live_number_html(data['switchyard_health'])}%</b><i><em style="width:{data['switchyard_health']:.1f}%"></em></i></div>
              </div>
            </div>
            ''', unsafe_allow_html=True)
        with b:
            st.markdown(f'''
            <div class="panel exec-panel filled-panel">
              <div class="panel-title"><h3>🕒 Operational Timeline</h3><span>Latest Events • Live</span></div>
              <div class="timeline-live">
                <div class="event-line"><b>10:24</b><span>Reservoir level stable in normal operating zone</span><em>NORMAL</em></div>
                <div class="event-line"><b>10:17</b><span>Unit #2 bearing temperature returned to baseline</span><em>RECOVERED</em></div>
                <div class="event-line"><b>09:58</b><span>Rainfall sensor indicates medium intensity</span><em>WATCH</em></div>
                <div class="event-line"><b>09:41</b><span>Switchyard export remains synchronized</span><em>NORMAL</em></div>
                <div class="event-line"><b>09:15</b><span>AI issued hydrology watch advisory</span><em>AI</em></div>
              </div>
              <div class="ai-box compact-ai"><div class="ai-title">Current Executive Reading</div><div class="ai-text">The plant is live and synchronized. Reservoir inflow, turbine dispatch, and electrical export remain aligned. No critical intervention is required.</div></div>
            </div>
            ''', unsafe_allow_html=True)
        with c:
            st.markdown(f'''
            <div class="panel exec-panel filled-panel">
              <div class="panel-title"><h3>📡 Asset Sensor Layer</h3><span>Live Asset Values</span></div>
              <div class="asset-live-grid">
                <div class="asset-live-card healthy"><div><b>🌊 Reservoir Level</b><span>{live_number_html(data['reservoir_level'], amp=.04, decimals=2)} m</span></div><em>Normal band</em></div>
                <div class="asset-live-card watch"><div><b>🟡 Piezometer PZ-07</b><span>{live_number_html(data['piezometer'], amp=.28, decimals=1)} kPa</span></div><em>Mild upward trend</em></div>
                <div class="asset-live-card healthy"><div><b>💦 Seepage SP-04</b><span>{live_number_html(data['seepage'], amp=.16, decimals=1)} L/min</span></div><em>Within baseline</em></div>
                <div class="asset-live-card healthy"><div><b>⚙️ Turbine Vibration U2</b><span>{live_number_html(data['vib'], amp=.03, decimals=2)} mm/s</span></div><em>Unit active</em></div>
                <div class="asset-live-card healthy"><div><b>🌡️ Transformer T1 Oil Temp</b><span>{live_number_html(data['bearing_temp'] + 8, amp=.20, decimals=1)} °C</span></div><em>Thermal normal</em></div>
                <div class="asset-live-card healthy"><div><b>🔌 Switchyard CB-02</b><span>CLOSED</span></div><em>Export synchronized</em></div>
              </div>
              <div class="metric-row"><div class="metric-name">🛰️ Data Quality</div><div class="metric-value">{live_number_html(99.7, amp=.04, decimals=1)}%</div></div>
              <div class="metric-row"><div class="metric-name">📶 Comms Status</div><div class="metric-value">MQTT Ready</div></div>
            </div>
            ''', unsafe_allow_html=True)


    elif page == "🎯 Vision & Architecture":
        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("Vision Achievement", "98.6", "%", "Sustainability translated into daily operation")
        with c2: kpi("Intelligence Domains", "6", "engines", "Safety, asset, energy, ESG, O&M, executive")
        with c3: kpi("Operational Outcome", "360", "°", "End-to-end visibility from water to grid")
        with c4: kpi("Executive Readiness", "NORMAL", "", "Decision layer ready for management review")
        left,right = st.columns([2.15,1])
        with left:
            st.markdown(intelligence_architecture_svg(), unsafe_allow_html=True)
        with right:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Platform Mission", "Vision → Intelligence → Outcome")
            st.markdown('''
            <div class="ai-box">
              <div class="ai-title">Mission Statement</div>
              <div class="ai-text" style="font-size:16px;font-weight:800;line-height:1.55;">
                Transform hydropower assets into a connected, intelligent, and sustainable operation.
              </div>
            </div>
            <div class="ai-box">
              <div class="ai-title">Strategic Translation</div>
              <div class="ai-text">
                HOIP converts corporate sustainability objectives into operational intelligence: safer dam operation, stronger asset reliability, optimized water utilization, predictive maintenance, ESG reporting, and executive decision support.
              </div>
            </div>
            ''', unsafe_allow_html=True)
            metric("Safe Dam Operation", "Safety Intelligence")
            metric("Asset Reliability", "Predictive O&M")
            metric("Water Optimization", "Hydrology + Dispatch")
            metric("ESG Reporting", "Environment + CO₂")
            metric("Executive Support", "KPI + Decision Brief")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="panel" style="margin-top:14px;">', unsafe_allow_html=True)
        header("Operational Excellence Outcomes", "Business value created by the platform")
        st.markdown('''
        <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:12px;">
          <div class="module-card" style="min-height:112px;"><div class="module-title">🛡 Safety</div><div class="module-text">Dam safety index, anomaly watch, operating risk visibility.</div></div>
          <div class="module-card" style="min-height:112px;"><div class="module-title">⚙ Asset</div><div class="module-text">Reliability baseline, early degradation signal, maintenance priority.</div></div>
          <div class="module-card" style="min-height:112px;"><div class="module-title">⚡ Energy</div><div class="module-text">Generation optimization, unit dispatch support, grid export awareness.</div></div>
          <div class="module-card" style="min-height:112px;"><div class="module-title">💧 Water</div><div class="module-text">Reservoir balance, inflow/outflow visibility, utilization strategy.</div></div>
          <div class="module-card" style="min-height:112px;"><div class="module-title">🌿 ESG</div><div class="module-text">Environmental compliance, CO₂ reduction, reporting automation.</div></div>
          <div class="module-card" style="min-height:112px;"><div class="module-title">📊 Executive</div><div class="module-text">KPI briefing, decision support, management-ready reporting.</div></div>
        </div>
        ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


    elif page == "🕸️ Subsystem Command Center":
        # Local live component: updates KPI, map, interpretations and heatmap without reloading the whole Streamlit app.
        components.html(subsystem_command_component(refresh_sec), height=1120, scrolling=False)

    elif page == "🗺️ Subsystem Coverage Map":
        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("Instrumented Assets", "127", "assets", "Civil, water, turbine, grid")
        with c2: kpi("Realtime Telemetry", "342", "tags", "Connected to HOIP layer")
        with c3: kpi("AI Analytics", "12+", "indices", "Safety, O&M, ESG, executive")
        with c4: kpi("Coverage", "100%", "domain", "End-to-end plant visibility")
        automation_matrix()


    elif page == "🌦️ Weather Station":
        weather_html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  :root{
    --bg:#041018; --panel:rgba(4,38,33,.78); --panel2:rgba(3,18,28,.78);
    --line:rgba(94,234,212,.28); --cyan:#5eead4; --green:#67e8a5; --gold:#ffd166;
    --text:#eef8ff; --muted:#a7cfc4; --blue:#7dd3fc;
  }
  *{box-sizing:border-box}
  body{margin:0;background:transparent;color:var(--text);font-family:Inter,Arial,sans-serif;overflow:hidden}
  .wx-wrap{width:100%;height:900px;padding:2px 0 0 0}
  .wx-kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:16px}
  .wx-kpi{
    min-height:146px;border:1px solid var(--line);border-radius:23px;padding:20px 22px;overflow:hidden;position:relative;
    background:linear-gradient(160deg,rgba(8,57,47,.78),rgba(4,22,30,.72));
    box-shadow:inset 0 1px 0 rgba(255,255,255,.05),0 18px 42px rgba(0,0,0,.22);
  }
  .wx-kpi:before{content:"";position:absolute;right:-35px;top:-38px;width:140px;height:140px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.22),transparent 68%)}
  .wx-kpi .label{font-size:12px;letter-spacing:.9px;text-transform:uppercase;color:var(--muted);font-weight:900}
  .wx-kpi .value{font-size:34px;font-weight:950;letter-spacing:-1px;margin-top:23px}
  .wx-kpi .unit{font-size:17px;color:#b6d8d0;margin-left:4px;font-weight:800}
  .wx-kpi .note{font-size:12px;color:#b6d8d0;margin-top:10px}
  .spark{height:2px;border-radius:99px;background:linear-gradient(90deg,rgba(94,234,212,.08),rgba(94,234,212,.86),rgba(103,232,165,.08));background-size:220% 100%;animation:spark 2s linear infinite;margin-top:18px}
  @keyframes spark{from{background-position:0 0}to{background-position:220% 0}}

  .wx-main{display:grid;grid-template-columns:1.62fr .98fr;gap:16px;height:690px}
  .panel{
    border:1px solid var(--line);border-radius:26px;position:relative;overflow:hidden;
    background:linear-gradient(160deg,rgba(7,54,45,.74),rgba(3,18,28,.70));
    box-shadow:0 22px 60px rgba(0,0,0,.24);backdrop-filter:blur(12px)
  }
  .panel:before{content:"";position:absolute;inset:0;background:
      radial-gradient(circle at 18% 8%,rgba(94,234,212,.12),transparent 28%),
      radial-gradient(circle at 72% 78%,rgba(255,209,102,.08),transparent 30%),
      repeating-linear-gradient(45deg,rgba(94,234,212,.04) 0 1px,transparent 1px 64px),
      repeating-linear-gradient(-45deg,rgba(94,234,212,.032) 0 1px,transparent 1px 64px);pointer-events:none}
  .panel>*{position:relative;z-index:1}
  .hero{padding:28px 32px}
  .title{font-size:28px;font-weight:950;letter-spacing:-.8px;line-height:1;margin:0}
  .subtitle{font-size:13px;color:#afd2ca;margin-top:10px;max-width:860px}
  .impact-chip{display:inline-flex;align-items:center;gap:8px;padding:8px 11px;border-radius:999px;border:1px solid rgba(103,232,165,.35);background:rgba(103,232,165,.11);font-size:11px;font-weight:900;color:#b8ffd6;text-transform:uppercase;margin-top:14px}
  .pulse-dot{width:8px;height:8px;border-radius:50%;background:#67e8a5;box-shadow:0 0 0 0 rgba(103,232,165,.62);animation:pulse 2.2s infinite}
  @keyframes pulse{70%{box-shadow:0 0 0 10px rgba(103,232,165,0)}}

  .flow-area{height:455px;margin-top:18px;position:relative;border-radius:26px;overflow:hidden;background:linear-gradient(160deg,rgba(1,21,31,.48),rgba(3,35,31,.30));border:1px solid rgba(94,234,212,.12)}
  .cloud{position:absolute;left:78px;top:82px;width:190px;height:92px;border-radius:54px;background:linear-gradient(180deg,rgba(130,231,255,.95),rgba(36,105,140,.72));box-shadow:0 0 45px rgba(125,211,252,.28),inset 0 1px 0 rgba(255,255,255,.35);animation:cloudFloat 4s ease-in-out infinite}
  .cloud:before{content:"";position:absolute;left:34px;top:-44px;width:88px;height:88px;border-radius:50%;background:inherit}
  .cloud:after{content:"";position:absolute;right:28px;top:-30px;width:74px;height:74px;border-radius:50%;background:inherit}
  @keyframes cloudFloat{50%{transform:translateY(-7px)}}
  .rain-layer{position:absolute;left:100px;top:178px;width:145px;height:105px;overflow:hidden}
  .drop{position:absolute;width:3px;height:24px;border-radius:99px;background:linear-gradient(180deg,transparent,#80f7ff);animation:rain 1.05s linear infinite;opacity:.85}
  .d1{left:5px;animation-delay:0s}.d2{left:28px;animation-delay:.2s}.d3{left:52px;animation-delay:.4s}.d4{left:84px;animation-delay:.12s}.d5{left:116px;animation-delay:.32s}.d6{left:140px;animation-delay:.55s}
  @keyframes rain{from{transform:translateY(-32px)}to{transform:translateY(126px)}}
  .sun{position:absolute;left:330px;top:91px;width:80px;height:80px;border-radius:50%;background:radial-gradient(circle,#fff3b0,#ffd166 55%,rgba(255,209,102,.10));box-shadow:0 0 46px rgba(255,209,102,.36);animation:sunPulse 3s ease-in-out infinite}
  @keyframes sunPulse{50%{box-shadow:0 0 68px rgba(255,209,102,.52);transform:scale(1.04)}}
  .wind{position:absolute;left:318px;top:218px;width:150px;height:70px;color:#baf7ff}
  .wind span{display:block;height:2px;border-radius:99px;background:linear-gradient(90deg,transparent,#a7f3ff,transparent);margin:14px 0;animation:wind 1.7s linear infinite}
  .wind span:nth-child(2){width:105px;margin-left:30px;animation-delay:.2s}.wind span:nth-child(3){width:132px;margin-left:8px;animation-delay:.44s}
  @keyframes wind{from{transform:translateX(-20px);opacity:.18}50%{opacity:1}to{transform:translateX(28px);opacity:.18}}
  .ai-core{position:absolute;left:472px;top:154px;width:188px;height:188px;border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;background:radial-gradient(circle at 44% 26%,rgba(94,234,212,.34),rgba(4,28,42,.94) 58%,rgba(3,13,24,.96));border:1px solid rgba(94,234,212,.52);box-shadow:0 0 42px rgba(94,234,212,.22),0 20px 55px rgba(0,0,0,.38)}
  .ai-core:before{content:"";position:absolute;inset:-18px;border:2px solid rgba(94,234,212,.18);border-radius:50%;animation:ring 5.2s linear infinite}
  .ai-core:after{content:"";position:absolute;inset:-34px;border:1px dashed rgba(94,234,212,.24);border-radius:50%;animation:ring 10s linear infinite reverse}
  @keyframes ring{to{transform:rotate(360deg)}}
  .ai-core b{font-size:14px;font-weight:950;color:#effff9;line-height:1.25;text-transform:uppercase;text-shadow:0 0 16px rgba(94,234,212,.65)}
  .outcome{position:absolute;width:162px;min-height:94px;border:1px solid rgba(94,234,212,.24);border-radius:22px;background:rgba(2,18,27,.78);box-shadow:0 18px 42px rgba(0,0,0,.28);padding:16px 14px;text-align:center;backdrop-filter:blur(10px)}
  .outcome .ico{font-size:24px}.outcome b{display:block;font-size:14px;margin-top:6px}.outcome small{display:block;color:#b6d8d0;font-size:11px;margin-top:5px}
  .res{left:744px;top:52px}.dam{left:760px;top:186px}.gen{left:745px;top:320px}.sed{left:552px;top:344px}
  .beam{position:absolute;height:4px;border-radius:99px;background:linear-gradient(90deg,transparent,rgba(94,234,212,.20),rgba(94,234,212,.98),rgba(255,209,102,.75),transparent);background-size:220% 100%;box-shadow:0 0 20px rgba(94,234,212,.45);animation:beam 2.2s linear infinite;transform-origin:left center;opacity:.9}
  .b1{left:245px;top:169px;width:254px;transform:rotate(-3deg)} .b2{left:404px;top:238px;width:145px;transform:rotate(-10deg)}
  .b3{left:654px;top:190px;width:132px;transform:rotate(-31deg)} .b4{left:660px;top:239px;width:126px;transform:rotate(1deg)}
  .b5{left:650px;top:285px;width:142px;transform:rotate(29deg)} .b6{left:590px;top:330px;width:52px;transform:rotate(60deg)}
  @keyframes beam{from{background-position:0 0}to{background-position:220% 0}}
  .ribbon{position:absolute;left:32px;right:32px;bottom:22px;height:66px;border-radius:20px;background:linear-gradient(90deg,rgba(6,58,50,.72),rgba(7,23,37,.72));border:1px solid rgba(94,234,212,.18);display:grid;grid-template-columns:repeat(5,1fr);align-items:center;gap:6px;padding:0 14px}
  .rib-item{text-align:center;font-weight:900;font-size:12px;color:#eafff8;position:relative}.rib-item span{display:block;color:#a7cfc4;font-weight:700;font-size:10px;margin-top:4px}
  .rib-item:not(:last-child):after{content:"";position:absolute;right:-14px;top:20px;width:26px;height:3px;border-radius:99px;background:linear-gradient(90deg,#5eead4,#ffd166);box-shadow:0 0 14px rgba(94,234,212,.5);animation:beam 2s linear infinite}

  .side{padding:24px}
  .side-title{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}.side-title h3{margin:0;font-size:18px}.side-title span{font-size:12px;color:#a7cfc4}
  .insight{border:1px solid rgba(94,234,212,.24);background:linear-gradient(145deg,rgba(52,211,153,.12),rgba(8,21,38,.42));border-radius:22px;padding:17px;margin-bottom:14px}
  .insight .head{font-size:12px;color:#7fffd4;font-weight:950;letter-spacing:.9px;text-transform:uppercase}
  .insight .big{font-size:32px;font-weight:950;margin-top:10px}.insight .tag{font-size:12px;color:#b8ffd6;font-weight:950;margin-left:8px}
  .insight p{font-size:14px;line-height:1.55;margin:12px 0 0;color:#e8f7ff}
  .metrics{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 16px}
  .mcard{border:1px solid rgba(94,234,212,.14);background:rgba(255,255,255,.035);border-radius:18px;padding:13px}
  .mcard span{display:block;color:#a7cfc4;font-size:11px;font-weight:900;text-transform:uppercase}.mcard b{display:block;font-size:19px;margin-top:8px}.mcard small{display:block;color:#b6d8d0;font-size:11px;margin-top:4px}
  .impact-grid{display:grid;gap:9px;margin-top:10px}
  .impact-row{display:grid;grid-template-columns:1fr auto;align-items:center;border-bottom:1px solid rgba(94,234,212,.10);padding:9px 0;font-size:13px}
  .impact-row b{font-size:12px;border-radius:999px;padding:5px 9px;background:rgba(103,232,165,.10);border:1px solid rgba(103,232,165,.25);color:#b8ffd6}
  .impact-row b.warn{background:rgba(255,209,102,.10);border-color:rgba(255,209,102,.28);color:#ffe6a6}
  .timeline{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:12px}
  .tcard{border:1px solid rgba(94,234,212,.12);background:rgba(255,255,255,.034);border-radius:16px;padding:11px;text-align:center}
  .tcard b{display:block;font-size:12px;color:#eafff8}.tcard span{display:block;color:#7fffd4;font-weight:950;font-size:17px;margin-top:6px}.tcard small{display:block;color:#a7cfc4;font-size:10px;margin-top:5px}
</style>
</head>
<body>
<div class="wx-wrap">
  <div class="wx-kpis">
    <div class="wx-kpi"><div class="label">Rainfall Driver</div><div class="value"><span id="rain">14.1</span><span class="unit">mm/h</span></div><div class="note" id="rainNote">Increasing catchment input</div><div class="spark"></div></div>
    <div class="wx-kpi"><div class="label">Inflow Forecast</div><div class="value">+<span id="inflow">3.2</span><span class="unit">%</span></div><div class="note">Expected 2–3 hours ahead</div><div class="spark"></div></div>
    <div class="wx-kpi"><div class="label">Flood Probability</div><div class="value"><span id="flood">LOW</span></div><div class="note">No immediate spillway alert</div><div class="spark"></div></div>
    <div class="wx-kpi"><div class="label">Generation Impact</div><div class="value"><span id="genImpact">STABLE</span></div><div class="note">Dispatch can be maintained</div><div class="spark"></div></div>
  </div>
  <div class="wx-main">
    <div class="panel hero">
      <h2 class="title">Weather Intelligence & Hydrological Forecast</h2>
      <div class="subtitle">Meteorological intelligence driving reservoir operation, dam safety watch, sediment risk, turbine dispatch, and grid export stability.</div>
      <div class="impact-chip"><span class="pulse-dot"></span> Live weather-to-operation correlation</div>
      <div class="flow-area">
        <div class="beam b1"></div><div class="beam b2"></div><div class="beam b3"></div><div class="beam b4"></div><div class="beam b5"></div><div class="beam b6"></div>
        <div class="cloud"></div>
        <div class="rain-layer"><span class="drop d1"></span><span class="drop d2"></span><span class="drop d3"></span><span class="drop d4"></span><span class="drop d5"></span><span class="drop d6"></span></div>
        <div class="sun"></div><div class="wind"><span></span><span></span><span></span></div>
        <div class="ai-core"><b>Weather<br>AI Correlation<br>Engine</b></div>
        <div class="outcome res"><div class="ico">💧</div><b>Reservoir</b><small id="resSmall">Moderate rise</small></div>
        <div class="outcome dam"><div class="ico">🛡️</div><b>Dam Safety</b><small id="damSmall">Normal watch</small></div>
        <div class="outcome gen"><div class="ico">⚡</div><b>Generation</b><small id="genSmall">Dispatch stable</small></div>
        <div class="outcome sed"><div class="ico">⛰️</div><b>Sediment</b><small id="sedSmall">Low transport</small></div>
        <div class="ribbon">
          <div class="rib-item">Rainfall<span>Upstream driver</span></div>
          <div class="rib-item">Reservoir<span>Storage response</span></div>
          <div class="rib-item">Dam Safety<span>Instrumentation watch</span></div>
          <div class="rib-item">Generation<span>Dispatch planning</span></div>
          <div class="rib-item">Grid Export<span>Stability impact</span></div>
        </div>
      </div>
    </div>
    <div class="panel side">
      <div class="side-title"><h3>Weather Analytics</h3><span>Operational interpretation</span></div>
      <div class="metrics">
        <div class="mcard"><span>Wind Speed</span><b><span id="wind">4.2</span> m/s</b><small>Normal crest condition</small></div>
        <div class="mcard"><span>Solar Radiation</span><b><span id="solar">633</span> W/m²</b><small>Daylight context</small></div>
        <div class="mcard"><span>Pressure</span><b><span id="pressure">1008.4</span> hPa</b><small>Stable trend</small></div>
        <div class="mcard"><span>Humidity</span><b><span id="hum">79</span>%</b><small>Rain persistence context</small></div>
      </div>
      <div class="insight">
        <div class="head">AI Weather Interpretation</div>
        <div class="big"><span id="risk">NORMAL</span><span class="tag" id="riskTag">LOW FLOOD RISK</span></div>
        <p id="aiText">Rainfall intensity is increasing but remains within normal operation band. Reservoir inflow is expected to rise moderately in the next 2–3 hours. No immediate dam safety concern.</p>
      </div>
      <div class="insight">
        <div class="head">Operational Impact</div>
        <div class="impact-grid">
          <div class="impact-row"><span>Reservoir Operation</span><b id="opRes">Moderate Rise</b></div>
          <div class="impact-row"><span>Dam Safety Watch</span><b id="opDam">Normal</b></div>
          <div class="impact-row"><span>Sediment Transport</span><b id="opSed">Low</b></div>
          <div class="impact-row"><span>Generation Dispatch</span><b id="opGen">Maintain</b></div>
          <div class="impact-row"><span>Operator Action</span><b id="opAct">No Action</b></div>
        </div>
      </div>
      <div class="insight">
        <div class="head">Forecast Timeline</div>
        <div class="timeline">
          <div class="tcard"><b>Now</b><span id="tNow">14.1</span><small>mm/h rain</small></div>
          <div class="tcard"><b>+30 min</b><span id="t30">15.2</span><small>mm/h rain</small></div>
          <div class="tcard"><b>+2 hr</b><span id="t2h">+3.2%</span><small>inflow</small></div>
          <div class="tcard"><b>+6 hr</b><span id="t6h">LOW</span><small>flood risk</small></div>
        </div>
      </div>
    </div>
  </div>
</div>
<script>
const $=id=>document.getElementById(id);
function clamp(v,a,b){return Math.max(a,Math.min(b,v))}
function wave(base,amp,period,phase=0){return base+amp*Math.sin((Date.now()/1000+phase)/period)}
function set(id,val){const e=$(id); if(e) e.textContent=val}
function update(){
  const rain=clamp(wave(14.1,4.5,5.5,.4),6.2,23.5);
  const wind=clamp(wave(4.2,1.1,7.0,1.7),2.4,6.2);
  const solar=clamp(wave(633,70,9.0,2.1),480,760);
  const hum=clamp(wave(79,5,7.8,.8),68,88);
  const pressure=clamp(wave(1008.4,2.6,11.0,1.2),1003.8,1012.7);
  const inflow=clamp((rain-9.5)*.72,0.8,9.8);
  let flood='LOW', gen='STABLE', risk='NORMAL', tag='LOW FLOOD RISK';
  let opRes='Moderate Rise', opDam='Normal', opSed='Low', opGen='Maintain', opAct='No Action';
  let ai=`Rainfall intensity is ${rain.toFixed(1)} mm/h and is acting as the upstream driver for reservoir inflow. Expected inflow response is +${inflow.toFixed(1)}% within 2–3 hours. Dam safety remains normal and generation dispatch can be maintained.`;
  if(rain>18){
    flood='WATCH'; gen='STABLE'; risk='WATCH'; tag='HYDROLOGY WATCH';
    opRes='Rising'; opSed='Moderate'; opAct='Review 30 min';
    ai=`Rainfall intensity has increased to ${rain.toFixed(1)} mm/h. Reservoir inflow is expected to rise +${inflow.toFixed(1)}% within 2–3 hours. Maintain generation dispatch, increase hydrology watch, and reassess spillway readiness in 30 minutes.`;
  }
  if(rain>21){
    flood='MED'; risk='ALERT'; tag='FLOOD WATCH';
    opRes='Fast Rise'; opDam='Enhanced Watch'; opSed='Moderate'; opGen='Maintain/Review'; opAct='Hydro Review';
  }
  set('rain',rain.toFixed(1)); set('wind',wind.toFixed(1)); set('solar',solar.toFixed(0)); set('hum',hum.toFixed(0)); set('pressure',pressure.toFixed(1));
  set('inflow',inflow.toFixed(1)); set('flood',flood); set('genImpact',gen); set('risk',risk); set('riskTag',tag); set('aiText',ai);
  set('opRes',opRes); set('opDam',opDam); set('opSed',opSed); set('opGen',opGen); set('opAct',opAct);
  set('resSmall',opRes); set('damSmall',opDam); set('sedSmall',opSed); set('genSmall',opGen);
  set('tNow',rain.toFixed(1)); set('t30',(rain+1.1).toFixed(1)); set('t2h','+'+inflow.toFixed(1)+'%'); set('t6h',flood);
  set('rainNote', rain>18 ? 'Hydrology watch active' : 'Increasing catchment input');
  ['opRes','opDam','opSed','opGen','opAct'].forEach(id=>{const e=$(id); if(e){e.className=(rain>18 && (id==='opRes'||id==='opSed'||id==='opAct'))?'warn':''}})
}
update(); setInterval(update,2000);
</script>
</body>
</html>
"""
        components.html(weather_html, height=905, scrolling=False)

    elif page == "🌫️ Air Quality Station":
        air_html = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
*{box-sizing:border-box} body{margin:0;background:transparent;color:#eef7ff;font-family:Inter,Arial,sans-serif;overflow:hidden}.wrap{padding:0 0 8px 0}.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:0 0 18px 0}.kpi{min-height:132px;border:1px solid rgba(94,234,212,.23);border-radius:24px;padding:18px 20px;background:linear-gradient(155deg,rgba(8,61,48,.82),rgba(3,24,33,.72));box-shadow:0 18px 44px rgba(0,0,0,.23),inset 0 1px 0 rgba(255,255,255,.045);position:relative;overflow:hidden}.kpi:before{content:"";position:absolute;right:-36px;top:-40px;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.25),transparent 70%)}.kl{font-size:12px;color:#a7cfc4;font-weight:900;letter-spacing:1px;text-transform:uppercase}.kv{font-size:32px;font-weight:950;letter-spacing:-1px;margin-top:16px;color:#f2fff9}.ku{font-size:16px;color:#a8d4cc;margin-left:4px;font-weight:800}.kn{font-size:12px;color:#b7d2cc;margin-top:12px}.spark{height:2px;margin-top:16px;border-radius:99px;background:linear-gradient(90deg,rgba(94,234,212,.06),rgba(94,234,212,.88),rgba(255,209,102,.25),rgba(94,234,212,.06));background-size:240% 100%;animation:spark 2.2s linear infinite}@keyframes spark{from{background-position:0 0}to{background-position:240% 0}}.grid{display:grid;grid-template-columns:1.45fr .95fr;gap:18px}.panel{border:1px solid rgba(94,234,212,.20);border-radius:26px;background:linear-gradient(160deg,rgba(4,47,39,.76),rgba(2,17,27,.72));box-shadow:0 22px 58px rgba(0,0,0,.25);position:relative;overflow:hidden}.hero{height:610px;padding:28px 32px;background:radial-gradient(circle at 20% 20%,rgba(94,234,212,.16),transparent 28%),radial-gradient(circle at 64% 52%,rgba(255,209,102,.12),transparent 32%),linear-gradient(160deg,rgba(5,50,43,.82),rgba(2,17,27,.74))}.hero:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(45deg,rgba(94,234,212,.04) 0 1px,transparent 1px 62px),repeating-linear-gradient(-45deg,rgba(94,234,212,.03) 0 1px,transparent 1px 62px)}.title{position:relative;z-index:4;font-size:26px;font-weight:950;letter-spacing:-.5px;color:#f2fff9}.sub{position:relative;z-index:4;font-size:13px;color:#b7d2cc;margin-top:8px;max-width:760px;line-height:1.45}.stage{position:absolute;inset:105px 22px 18px 22px;z-index:3}.station{position:absolute;left:70px;top:150px;width:190px;height:190px;border-radius:50%;background:radial-gradient(circle at 42% 30%,#19686d,#0b2941 62%,#071725);border:1px solid rgba(94,234,212,.42);box-shadow:0 22px 70px rgba(0,0,0,.34),0 0 55px rgba(94,234,212,.22);display:flex;align-items:center;justify-content:center;animation:float 4s ease-in-out infinite}.station:before{content:"";position:absolute;inset:-26px;border-radius:50%;border:2px solid rgba(94,234,212,.14);animation:ring 3.2s ease-out infinite}.station b{font-size:18px;color:#8ffff0;text-shadow:0 0 14px rgba(143,255,240,.8)}.station small{position:absolute;bottom:43px;color:#c8fff4;font-size:12px;font-weight:800}.sensor{position:absolute;width:122px;height:122px;border-radius:28px;background:rgba(5,31,42,.82);border:1px solid rgba(94,234,212,.24);box-shadow:0 18px 36px rgba(0,0,0,.28);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;backdrop-filter:blur(8px)}.sensor .ico{font-size:26px;margin-bottom:6px}.sensor b{font-size:12px;color:#eef7ff}.sensor span{font-size:16px;font-weight:950;color:#8ffff0;margin-top:7px}.s1{left:45px;top:10px}.s2{left:275px;top:25px}.s3{left:60px;top:385px}.s4{left:320px;top:380px}.asset{position:absolute;width:165px;height:88px;border-radius:22px;background:linear-gradient(140deg,rgba(255,209,102,.14),rgba(5,36,44,.86));border:1px solid rgba(255,209,102,.32);box-shadow:0 18px 42px rgba(0,0,0,.32),0 0 30px rgba(255,209,102,.12);padding:14px 16px}.asset b{font-size:13px;color:#ffd166;text-transform:uppercase}.asset small{display:block;font-size:11px;color:#d3e7e4;margin-top:6px;line-height:1.35}.a1{right:130px;top:28px}.a2{right:18px;top:178px}.a3{right:154px;top:330px}.a4{right:17px;top:456px}.flow{position:absolute;height:4px;border-radius:99px;background:linear-gradient(90deg,transparent,rgba(94,234,212,.22),rgba(94,234,212,.90),rgba(255,209,102,.50),transparent);background-size:220% 100%;box-shadow:0 0 18px rgba(94,234,212,.35);animation:beam 2.1s linear infinite;transform-origin:left center}.f1{left:220px;top:190px;width:410px;transform:rotate(-20deg)}.f2{left:222px;top:244px;width:490px;transform:rotate(0deg)}.f3{left:222px;top:294px;width:390px;transform:rotate(20deg)}.f4{left:225px;top:332px;width:485px;transform:rotate(34deg)}.plume{position:absolute;left:30px;top:95px;width:650px;height:340px;pointer-events:none;filter:blur(.2px)}.particle{position:absolute;width:7px;height:7px;border-radius:50%;background:rgba(180,255,245,.62);box-shadow:0 0 14px rgba(94,234,212,.70);animation:drift 5.2s linear infinite}.particle:nth-child(2){animation-delay:-.8s;top:20px}.particle:nth-child(3){animation-delay:-1.6s;top:90px}.particle:nth-child(4){animation-delay:-2.4s;top:155px}.particle:nth-child(5){animation-delay:-3.2s;top:225px}.particle:nth-child(6){animation-delay:-4s;top:290px}@keyframes drift{from{left:110px;opacity:.05;transform:translateY(0)}25%{opacity:.75}to{left:650px;opacity:.05;transform:translateY(-46px)}}@keyframes beam{from{background-position:0 0}to{background-position:220% 0}}@keyframes ring{0%{opacity:.7;transform:scale(.78)}100%{opacity:0;transform:scale(1.34)}}@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}.side{min-height:610px;padding:22px}.pt{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}.pt h3{margin:0;font-size:18px;font-weight:950}.pt span{font-size:12px;color:#a7cfc4}.ai{border:1px solid rgba(94,234,212,.26);border-radius:22px;padding:17px 18px;background:linear-gradient(145deg,rgba(94,234,212,.12),rgba(8,21,38,.50));margin-bottom:14px}.bt{font-size:12px;color:#8ffff0;font-weight:950;letter-spacing:.9px;text-transform:uppercase;margin-bottom:10px}.big{font-size:35px;font-weight:950;color:#f2fff9;letter-spacing:-1px}.stat{font-size:13px;font-weight:950;color:#9dffc8;margin-left:8px}.txt{font-size:14px;color:#e8f7ff;line-height:1.58}.risk-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 14px}.risk{border:1px solid rgba(94,234,212,.16);border-radius:18px;padding:12px;background:rgba(255,255,255,.04)}.risk small{display:block;color:#a7cfc4;font-size:11px}.risk b{display:block;margin-top:6px;color:#fff;font-size:15px}.meter{margin:13px 0}.mh{display:flex;justify-content:space-between;font-size:12px;color:#c7d9e9;margin-bottom:6px}.mb{height:10px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden}.mf{height:100%;border-radius:99px;background:linear-gradient(90deg,#34d399,#5eead4,#ffd166);transition:width .5s}.timeline{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:12px}.slot{border:1px solid rgba(94,234,212,.16);border-radius:16px;padding:11px;background:rgba(255,255,255,.04);text-align:center}.slot b{display:block;color:#8ffff0;font-size:11px}.slot span{display:block;font-size:16px;font-weight:950;margin-top:7px}.bottom{margin-top:18px;padding:18px 20px}.chips{display:flex;gap:10px;flex-wrap:wrap}.chip{border:1px solid rgba(94,234,212,.20);border-radius:999px;padding:9px 13px;background:rgba(255,255,255,.045);font-size:12px;color:#d7fff5}.chip b{color:#8ffff0}
</style></head><body><div class="wrap"><div class="kpis"><div class="kpi"><div class="kl">AQI HEALTH</div><div class="kv"><span id="aqi">96.8</span><span class="ku">%</span></div><div class="kn"><span id="aqiNote">GOOD • environmental condition normal</span></div><div class="spark"></div></div><div class="kpi"><div class="kl">PM2.5</div><div class="kv"><span id="pm25">__PM25__</span><span class="ku">µg/m³</span></div><div class="kn">Fine particulate exposure</div><div class="spark"></div></div><div class="kpi"><div class="kl">PM10 / DUST</div><div class="kv"><span id="pm10">__PM10__</span><span class="ku">µg/m³</span></div><div class="kn"><span id="dustNote">LOW construction dust watch</span></div><div class="spark"></div></div><div class="kpi"><div class="kl">ESG COMPLIANCE</div><div class="kv"><span id="esg">97.2</span><span class="ku">%</span></div><div class="kn">Community + operational reporting</div><div class="spark"></div></div></div><div class="grid"><div class="panel hero"><div class="title">Air Quality & Environmental Intelligence Center</div><div class="sub">Real-time environmental context for dam perimeter, construction dust, equipment contamination risk, powerhouse ventilation and ESG reporting.</div><div class="stage"><div class="plume"><div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div></div><div class="sensor s1"><div class="ico">🌫️</div><b>PM2.5</b><span id="pm25b">__PM25__</span></div><div class="sensor s2"><div class="ico">🧱</div><b>PM10 Dust</b><span id="pm10b">__PM10__</span></div><div class="sensor s3"><div class="ico">🌬️</div><b>Wind</b><span id="wind">__WIND__ m/s</span></div><div class="sensor s4"><div class="ico">💧</div><b>Humidity</b><span id="hum">__HUM__%</span></div><div class="station"><b>AQS-01</b><small>Perimeter Station</small></div><div class="flow f1"></div><div class="flow f2"></div><div class="flow f3"></div><div class="flow f4"></div><div class="asset a1"><b>Cooling Intake</b><small>filter loading & ventilation impact</small></div><div class="asset a2"><b>Switchyard</b><small>insulator dust contamination watch</small></div><div class="asset a3"><b>Solar / CCTV</b><small>surface fouling & visibility context</small></div><div class="asset a4"><b>Community ESG</b><small>perimeter exposure & reporting</small></div></div></div><div class="panel side"><div class="pt"><h3>Environmental Interpretation</h3><span>dam area impact</span></div><div class="ai"><div class="bt">AI Environmental Advisor</div><div class="txt"><div><span class="big" id="riskLevel">LOW</span><span class="stat" id="riskStat">NO RESTRICTION</span></div><span id="aiText">Air quality remains acceptable for normal hydropower operation. Dust dispersion is controlled by current wind condition and no powerhouse ventilation restriction is required.</span></div></div><div class="risk-grid"><div class="risk"><small>Powerhouse Ventilation</small><b id="ventRisk">Normal</b></div><div class="risk"><small>Outdoor Switchyard</small><b id="swRisk">Low Dust Risk</b></div><div class="risk"><small>Solar / CCTV Fouling</small><b id="camRisk">Moderate Watch</b></div><div class="risk"><small>Community Exposure</small><b id="comRisk">Low</b></div></div><div class="bt">Infrastructure Contamination Risk</div><div class="meter"><div class="mh"><span>Cooling Intake Filter</span><b><span id="cool">12</span>%</b></div><div class="mb"><div class="mf" id="coolBar" style="width:12%"></div></div></div><div class="meter"><div class="mh"><span>Switchyard Insulator Dust</span><b><span id="switch">21</span>%</b></div><div class="mb"><div class="mf" id="switchBar" style="width:21%"></div></div></div><div class="meter"><div class="mh"><span>Solar Panel / Camera Lens Fouling</span><b><span id="foul">42</span>%</b></div><div class="mb"><div class="mf" id="foulBar" style="width:42%"></div></div></div><div class="ai"><div class="bt">6-Hour Environmental Forecast</div><div class="timeline"><div class="slot"><b>NOW</b><span id="h0">GOOD</span></div><div class="slot"><b>+2H</b><span id="h2">GOOD</span></div><div class="slot"><b>+4H</b><span id="h4">MOD</span></div><div class="slot"><b>+6H</b><span id="h6">GOOD</span></div></div></div></div></div><div class="panel bottom"><div class="pt"><h3>Operational Impact Summary</h3><span>environmental data translated into hydropower action</span></div><div class="chips"><div class="chip"><b>Generation:</b> no impact</div><div class="chip"><b>Dam Safety:</b> normal</div><div class="chip"><b>Construction:</b> continue with dust watch</div><div class="chip"><b>Maintenance:</b> inspect outdoor lens/filter weekly</div><div class="chip"><b>ESG:</b> trend included in monthly report</div></div></div></div><script>
const $=id=>document.getElementById(id);function clamp(v,a,b){return Math.max(a,Math.min(b,v))}function wave(b,a,p,ph=0){return b+a*Math.sin((Date.now()/1000+ph)/p)}function set(id,val){const e=$(id);if(e)e.textContent=val}function width(id,val){const e=$(id);if(e)e.style.width=val+'%'}
function update(){let pm25=clamp(wave(__PM25__,4.8,6,1),8,31),pm10=clamp(wave(__PM10__,8.5,7,2),22,66),no2=clamp(wave(__NO2__,2.6,8,3),8,23),co=clamp(wave(__CO__,.09,9,1.5),.22,.68),wind=clamp(wave(__WIND__,1.2,6,2),2.2,6.8),hum=clamp(wave(__HUM__,5,7,1),65,90);let dust=clamp(pm10*1.18 - wind*3 + (hum<72?8:0),12,78),aqi=clamp(100-(pm25*.38+pm10*.12+no2*.10+co*3),86,98.8),esg=clamp(98.5-dust*.035,94,99);let level='LOW',stat='NO RESTRICTION',note='GOOD • environmental condition normal',dustNote='LOW construction dust watch',ai=`Air quality remains acceptable for normal hydropower operation. PM10 is ${pm10.toFixed(1)} µg/m³ and wind speed is ${wind.toFixed(1)} m/s, supporting dispersion away from critical assets. No powerhouse ventilation restriction is required.`;let vent='Normal',sw='Low Dust Risk',cam='Moderate Watch',com='Low';if(dust>48){level='WATCH';stat='MITIGATION ADVISED';note='WATCH • perimeter dust increasing';dustNote='MODERATE dust watch';ai=`PM10 is elevated at ${pm10.toFixed(1)} µg/m³ with wind-driven dispersion toward outdoor assets. Continue operation, increase road watering, and inspect camera lens or outdoor panel surfaces after shift.`;cam='High Watch';sw='Moderate Dust Watch'}if(dust>62){level='MODERATE';stat='FIELD ACTION';vent='Filter Watch';sw='Moderate / Inspect';com='Moderate';ai=`Environmental dust risk is moderate. Hydropower generation remains unaffected, but field mitigation is recommended: watering frequency, outdoor switchyard visual check, and HVAC filter observation.`}set('pm25',pm25.toFixed(1));set('pm25b',pm25.toFixed(1));set('pm10',pm10.toFixed(1));set('pm10b',pm10.toFixed(1));set('aqi',aqi.toFixed(1));set('esg',esg.toFixed(1));set('wind',wind.toFixed(1)+' m/s');set('hum',hum.toFixed(0)+'%');set('riskLevel',level);set('riskStat',stat);set('aiText',ai);set('aqiNote',note);set('dustNote',dustNote);set('ventRisk',vent);set('swRisk',sw);set('camRisk',cam);set('comRisk',com);let cool=clamp(dust*.32,8,38),swv=clamp(dust*.50,12,55),foul=clamp(dust*.78,22,80);set('cool',cool.toFixed(0));set('switch',swv.toFixed(0));set('foul',foul.toFixed(0));width('coolBar',cool);width('switchBar',swv);width('foulBar',foul);set('h0',dust>48?'WATCH':'GOOD');set('h2',dust>56?'WATCH':'GOOD');set('h4',dust>44?'MOD':'GOOD');set('h6',dust>60?'WATCH':'GOOD')}
update();setInterval(update,2000);
</script></body></html>
"""
        air_html = (air_html
            .replace('__PM25__', f"{data['pm25']:.1f}")
            .replace('__PM10__', f"{data['pm10']:.1f}")
            .replace('__NO2__', f"{data['no2']:.1f}")
            .replace('__CO__', f"{data['co']:.2f}")
            .replace('__WIND__', f"{data['wind_speed']:.1f}")
            .replace('__HUM__', f"{data['humidity']:.0f}")
        )
        components.html(air_html, height=940, scrolling=False)

    elif page == "💧 Water Quality Station":
        water_html = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
*{box-sizing:border-box}body{margin:0;background:transparent;color:#eef7ff;font-family:Inter,Arial,sans-serif;overflow:hidden}.wrap{padding:0 0 8px 0}.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:18px}.kpi{min-height:132px;border:1px solid rgba(94,234,212,.23);border-radius:24px;padding:18px 20px;background:linear-gradient(155deg,rgba(8,61,48,.82),rgba(3,24,33,.72));box-shadow:0 18px 44px rgba(0,0,0,.23),inset 0 1px 0 rgba(255,255,255,.045);position:relative;overflow:hidden}.kpi:before{content:"";position:absolute;right:-36px;top:-40px;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.25),transparent 70%)}.kl{font-size:12px;color:#a7cfc4;font-weight:900;letter-spacing:1px;text-transform:uppercase}.kv{font-size:32px;font-weight:950;letter-spacing:-1px;margin-top:16px;color:#f2fff9}.ku{font-size:16px;color:#a8d4cc;margin-left:4px;font-weight:800}.kn{font-size:12px;color:#b7d2cc;margin-top:12px}.spark{height:2px;margin-top:16px;border-radius:99px;background:linear-gradient(90deg,rgba(94,234,212,.06),rgba(94,234,212,.88),rgba(255,209,102,.30),rgba(94,234,212,.06));background-size:240% 100%;animation:spark 2.2s linear infinite}@keyframes spark{from{background-position:0 0}to{background-position:240% 0}}.grid{display:grid;grid-template-columns:1.45fr .95fr;gap:18px}.panel{border:1px solid rgba(94,234,212,.20);border-radius:26px;background:linear-gradient(160deg,rgba(4,47,39,.76),rgba(2,17,27,.72));box-shadow:0 22px 58px rgba(0,0,0,.25);position:relative;overflow:hidden}.hero{height:650px;padding:28px 32px;background:radial-gradient(circle at 19% 14%,rgba(94,234,212,.16),transparent 28%),radial-gradient(circle at 66% 58%,rgba(255,209,102,.11),transparent 32%),linear-gradient(160deg,rgba(5,50,43,.82),rgba(2,17,27,.74))}.hero:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(45deg,rgba(94,234,212,.04) 0 1px,transparent 1px 62px),repeating-linear-gradient(-45deg,rgba(94,234,212,.03) 0 1px,transparent 1px 62px)}.title{position:relative;z-index:4;font-size:26px;font-weight:950;letter-spacing:-.5px;color:#f2fff9}.sub{position:relative;z-index:4;font-size:13px;color:#b7d2cc;margin-top:8px;max-width:810px;line-height:1.45}.stage{position:absolute;inset:104px 22px 18px 22px;z-index:3}.reservoir{position:absolute;left:26px;top:72px;width:610px;height:468px;border-radius:28px;background:linear-gradient(180deg,rgba(22,117,157,.34) 0 20%,rgba(34,211,238,.34) 21%,rgba(45,212,191,.20) 58%,rgba(9,31,45,.60) 100%);border:1px solid rgba(94,234,212,.22);overflow:hidden;box-shadow:inset 0 0 65px rgba(94,234,212,.10),0 18px 45px rgba(0,0,0,.22)}.waterline{position:absolute;left:-6%;right:-6%;top:126px;height:22px;border-radius:50%;background:linear-gradient(90deg,rgba(127,255,212,.14),rgba(94,234,212,.75),rgba(127,255,212,.14));filter:blur(.2px);animation:wave 3.2s ease-in-out infinite}.reservoir:before{content:"SURFACE LAYER";position:absolute;top:28px;left:26px;color:#a7cfc4;font-size:11px;font-weight:900;letter-spacing:.8px}.reservoir:after{content:"BOTTOM SEDIMENT LAYER";position:absolute;bottom:22px;left:26px;color:#ffd166;font-size:11px;font-weight:900;letter-spacing:.8px}.layer{position:absolute;left:30px;right:210px;border:1px solid rgba(94,234,212,.14);background:rgba(255,255,255,.035);border-radius:22px;padding:14px 16px}.l1{top:55px}.l2{top:184px}.l3{bottom:50px}.layer b{display:block;font-size:14px;color:#eef7ff;margin-bottom:8px}.chips{display:flex;flex-wrap:wrap;gap:8px}.chip{border:1px solid rgba(94,234,212,.20);border-radius:999px;background:rgba(255,255,255,.05);padding:7px 10px;font-size:12px;color:#d8fff6;font-weight:800}.sedcloud{position:absolute;left:235px;bottom:78px;width:230px;height:118px;border-radius:48% 52% 46% 54%;background:radial-gradient(circle at 20% 38%,rgba(255,209,102,.45),transparent 17%),radial-gradient(circle at 43% 54%,rgba(255,209,102,.34),transparent 20%),radial-gradient(circle at 70% 44%,rgba(255,209,102,.28),transparent 22%);filter:blur(1px);opacity:.88;animation:sed 5s ease-in-out infinite}.intake{position:absolute;right:42px;top:166px;width:138px;height:250px;border:1px solid rgba(94,234,212,.28);border-radius:26px;background:linear-gradient(180deg,rgba(8,53,62,.88),rgba(5,24,36,.90));box-shadow:0 20px 42px rgba(0,0,0,.30)}.intake:before{content:"TURBINE INTAKE";position:absolute;top:18px;left:14px;right:14px;text-align:center;font-size:11px;color:#8ffff0;font-weight:950;letter-spacing:.7px}.intake:after{content:"";position:absolute;left:22px;right:22px;top:70px;height:125px;border-radius:14px;background:repeating-linear-gradient(90deg,rgba(94,234,212,.48) 0 4px,transparent 4px 16px);opacity:.65}.arrow{position:absolute;height:4px;border-radius:99px;background:linear-gradient(90deg,transparent,rgba(94,234,212,.25),rgba(94,234,212,.92),rgba(255,209,102,.46),transparent);background-size:220% 100%;box-shadow:0 0 18px rgba(94,234,212,.35);animation:beam 2s linear infinite}.a1{left:454px;top:309px;width:170px;transform:rotate(-5deg)}.a2{left:455px;top:372px;width:170px;transform:rotate(5deg)}.score{position:absolute;right:38px;top:35px;width:200px;border:1px solid rgba(94,234,212,.24);border-radius:24px;background:rgba(2,20,30,.74);padding:18px;backdrop-filter:blur(8px)}.score small{display:block;color:#a7cfc4;font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.8px}.score b{display:block;font-size:44px;line-height:1;color:#f2fff9;letter-spacing:-1.6px;margin-top:8px}.score span{display:inline-flex;margin-top:10px;color:#9dffc8;font-weight:950}.corr{position:absolute;left:34px;right:34px;bottom:26px;border:1px solid rgba(94,234,212,.20);border-radius:22px;background:rgba(2,18,26,.78);padding:16px 18px}.corr b{font-size:12px;text-transform:uppercase;color:#8ffff0;letter-spacing:.8px}.ribbon{display:grid;grid-template-columns:repeat(6,1fr);gap:6px;align-items:center;margin-top:12px}.step{font-size:12px;text-align:center;color:#e8f7ff;font-weight:850}.beamstep{height:4px;border-radius:99px;background:linear-gradient(90deg,#34d399,#5eead4,#ffd166);background-size:200% 100%;animation:beam 1.7s linear infinite}.side{min-height:650px;padding:22px}.pt{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}.pt h3{margin:0;font-size:18px;font-weight:950}.pt span{font-size:12px;color:#a7cfc4}.ai{border:1px solid rgba(94,234,212,.26);border-radius:22px;padding:17px 18px;background:linear-gradient(145deg,rgba(94,234,212,.12),rgba(8,21,38,.50));margin-bottom:14px}.bt{font-size:12px;color:#8ffff0;font-weight:950;letter-spacing:.9px;text-transform:uppercase;margin-bottom:10px}.big{font-size:35px;font-weight:950;color:#f2fff9;letter-spacing:-1px}.stat{font-size:13px;font-weight:950;color:#9dffc8;margin-left:8px}.txt{font-size:14px;color:#e8f7ff;line-height:1.58}.impact{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 14px}.risk{border:1px solid rgba(94,234,212,.16);border-radius:18px;padding:12px;background:rgba(255,255,255,.04)}.risk small{display:block;color:#a7cfc4;font-size:11px}.risk b{display:block;margin-top:6px;color:#fff;font-size:15px}.meter{margin:13px 0}.mh{display:flex;justify-content:space-between;font-size:12px;color:#c7d9e9;margin-bottom:6px}.mb{height:10px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden}.mf{height:100%;border-radius:99px;background:linear-gradient(90deg,#34d399,#5eead4,#ffd166);transition:width .5s}.bottom{margin-top:18px;padding:18px 20px}.bottom .chips{display:flex;gap:10px;flex-wrap:wrap}.bottom .chip{border:1px solid rgba(94,234,212,.20);border-radius:999px;background:rgba(255,255,255,.045);padding:10px 13px;color:#dffbf1;font-size:13px}.bottom .chip b{color:#8ffff0}@keyframes wave{0%,100%{transform:translateX(0) scaleY(1)}50%{transform:translateX(14px) scaleY(.82)}}@keyframes sed{0%,100%{transform:translate(0,0) scale(1);opacity:.70}50%{transform:translate(22px,-10px) scale(1.12);opacity:.95}}@keyframes beam{from{background-position:0 0}to{background-position:220% 0}}
</style></head><body><div class="wrap"><div class="kpis"><div class="kpi"><div class="kl">WATER QUALITY INDEX</div><div class="kv"><span id="wqi">96.8</span><span class="ku">/100</span></div><div class="kn"><span id="wqiNote">EXCELLENT • operation-ready</span></div><div class="spark"></div></div><div class="kpi"><div class="kl">TURBIDITY</div><div class="kv"><span id="turbK">__TURB__</span><span class="ku">NTU</span></div><div class="kn"><span id="sedNote">Moderate sediment signal</span></div><div class="spark"></div></div><div class="kpi"><div class="kl">WATER CHEMISTRY</div><div class="kv"><span id="phK">__PH__</span><span class="ku">pH</span></div><div class="kn">Neutral • low corrosion potential</div><div class="spark"></div></div><div class="kpi"><div class="kl">IRRIGATION SUITABILITY</div><div class="kv"><span id="irr">GOOD</span></div><div class="kn">Downstream use acceptable</div><div class="spark"></div></div></div><div class="grid"><div class="panel hero"><div class="title">Reservoir Water Quality Intelligence Center</div><div class="sub">Water chemistry, turbidity, dissolved oxygen and conductivity translated into turbine, sedimentation, irrigation and ESG operational decisions.</div><div class="stage"><div class="reservoir"><div class="waterline"></div><div class="layer l1"><b>Surface Layer</b><div class="chips"><span class="chip">Temp <span id="temp">__TEMP__</span> °C</span><span class="chip">pH <span id="phSmall">__PH__</span></span><span class="chip">DO <span id="doSmall">__DO__</span> mg/L</span></div></div><div class="layer l2"><b>Water Column</b><div class="chips"><span class="chip">Conductivity <span id="ecSmall">__EC__</span> µS/cm</span><span class="chip">Mixing Stable</span><span class="chip">No bloom signal</span></div></div><div class="layer l3"><b>Sediment Layer</b><div class="chips"><span class="chip">Turbidity <span id="turbSmall">__TURB__</span> NTU</span><span class="chip" id="siltChip">Low siltation risk</span></div></div><div class="sedcloud"></div><div class="intake"></div><div class="arrow a1"></div><div class="arrow a2"></div></div><div class="score"><small>Water Intelligence Score</small><b id="score">96.8</b><span id="scoreLabel">EXCELLENT</span></div><div class="corr"><b>Water Quality Driver Chain</b><div class="ribbon"><div class="step">Rainfall</div><div class="beamstep"></div><div class="step">Inflow</div><div class="beamstep"></div><div class="step">Turbidity</div><div class="beamstep"></div><div class="step">Sediment</div><div class="beamstep"></div><div class="step">Intake</div><div class="beamstep"></div><div class="step">Turbine</div></div></div></div></div><div class="panel side"><div class="pt"><h3>Water Intelligence Interpretation</h3><span>reservoir • intake • downstream</span></div><div class="ai"><div class="bt">AI Water Advisor</div><div class="txt"><div><span class="big" id="riskLevel">GOOD</span><span class="stat" id="riskStat">NO RESTRICTION</span></div><span id="aiText">Reservoir water quality remains inside operational envelope. No sediment flushing, no corrosion concern and no irrigation restriction are required.</span></div></div><div class="impact"><div class="risk"><small>Turbine Abrasion</small><b id="abrRisk">Low</b></div><div class="risk"><small>Intake Sediment</small><b id="intakeRisk">Normal</b></div><div class="risk"><small>Cooling Water</small><b id="coolRisk">Good</b></div><div class="risk"><small>ESG / Irrigation</small><b id="esgRisk">Pass</b></div></div><div class="bt">Operational Risk Translation</div><div class="meter"><div class="mh"><span>Turbine Abrasion Risk</span><b><span id="abr">12</span>%</b></div><div class="mb"><div class="mf" id="abrBar" style="width:12%"></div></div></div><div class="meter"><div class="mh"><span>Reservoir Siltation Signal</span><b><span id="silt">18</span>%</b></div><div class="mb"><div class="mf" id="siltBar" style="width:18%"></div></div></div><div class="meter"><div class="mh"><span>Corrosion / Scaling Potential</span><b><span id="corrRisk">9</span>%</b></div><div class="mb"><div class="mf" id="corrBar" style="width:9%"></div></div></div><div class="ai"><div class="bt">Sedimentation Intelligence</div><div class="txt" id="sedText">Current turbidity indicates moderate suspended sediment after upstream runoff, with no accelerated reservoir siltation signal.</div></div><div class="ai"><div class="bt">Ecology & Irrigation Insight</div><div class="txt" id="ecoText">Dissolved oxygen and neutral pH support aquatic health. Downstream irrigation suitability remains good.</div></div></div></div><div class="panel bottom"><div class="pt"><h3>Executive Insight</h3><span>water data translated into decision</span></div><div class="chips"><div class="chip"><b>Turbine:</b> <span id="bTurb">no efficiency impact</span></div><div class="chip"><b>Sediment:</b> <span id="bSed">no flushing required</span></div><div class="chip"><b>Pollution:</b> <span id="bPol">no indication</span></div><div class="chip"><b>Irrigation:</b> <span id="bIrr">suitable</span></div><div class="chip"><b>ESG:</b> compliance maintained</div></div></div></div><script>
const $=id=>document.getElementById(id);function clamp(v,a,b){return Math.max(a,Math.min(b,v))}function wave(b,a,p,ph=0){return b+a*Math.sin((Date.now()/1000+ph)/p)}function set(id,val){const e=$(id);if(e)e.textContent=val}function width(id,val){const e=$(id);if(e)e.style.width=val+'%'}
function update(){let ph=clamp(wave(__PH__,.10,7,1),6.92,7.38),turb=clamp(wave(__TURB__,5.8,6,2),12,42),doo=clamp(wave(__DO__,.34,8,3),6.7,8.2),ec=clamp(wave(__EC__,14,9,1.5),145,225),temp=clamp(wave(__TEMP__,.55,8,2.5),24.4,26.6);let turbRisk=clamp((turb-10)*1.15,6,58),silt=clamp(turb*1.05-5,8,62),cor=clamp(Math.abs(ph-7.1)*20+ec/22,5,24),wqi=clamp(100-(Math.abs(ph-7.15)*8+Math.max(0,turb-18)*.33+Math.abs(doo-7.5)*2+Math.max(0,ec-190)*.04),86,98.8);let level='GOOD',stat='NO RESTRICTION',label='EXCELLENT',sedNote='Moderate sediment signal',ai=`Reservoir water quality remains inside operational envelope. Turbidity is ${turb.toFixed(1)} NTU, pH is neutral, DO is ${doo.toFixed(1)} mg/L and conductivity remains low; turbine intake operation can continue normally.`;let abr='Low',intake='Normal',cool='Good',esg='Pass',siltChip='Low siltation risk',bTurb='no efficiency impact',bSed='no flushing required',bPol='no indication',bIrr='suitable';let sedText=`Turbidity at ${turb.toFixed(1)} NTU indicates moderate suspended sediment. No accelerated reservoir siltation signal; bathymetry survey is not required.`;if(turb>30){level='WATCH';stat='SEDIMENT WATCH';label='GOOD / WATCH';sedNote='Sediment transport increasing';abr='Moderate';intake='Sediment Watch';siltChip='Sediment watch';bSed='monitor intake / no flushing yet';ai=`Turbidity has increased to ${turb.toFixed(1)} NTU, likely driven by upstream runoff. Keep generation normal but watch intake sediment load and schedule visual inspection if trend persists.`;sedText=`Suspended sediment is increasing. Current condition does not require flushing, but repeated events may indicate early reservoir deposition trend.`}if(turb>38){level='MODERATE';stat='OPERATOR REVIEW';abr='Moderate / Inspect';intake='Inspection Watch';bTurb='abrasion watch';bSed='review sediment handling';sedText=`High turbidity episode detected. Potential sediment influx after runoff; recommend intake inspection and bathymetry verification if persistence exceeds operational threshold.`}let ecoText=doo<7?`Dissolved oxygen is trending lower but remains acceptable. Continue ecology watch and keep downstream use under normal advisory.`:`Dissolved oxygen and neutral pH support aquatic health. Downstream irrigation suitability remains good.`;set('wqi',wqi.toFixed(1));set('score',wqi.toFixed(1));set('scoreLabel',label);set('wqiNote',label+' • operation-ready');set('turbK',turb.toFixed(1));set('turbSmall',turb.toFixed(1));set('phK',ph.toFixed(2));set('phSmall',ph.toFixed(2));set('doSmall',doo.toFixed(1));set('ecSmall',ec.toFixed(0));set('temp',temp.toFixed(1));set('sedNote',sedNote);set('riskLevel',level);set('riskStat',stat);set('aiText',ai);set('abrRisk',abr);set('intakeRisk',intake);set('coolRisk',cool);set('esgRisk',esg);set('siltChip',siltChip);set('sedText',sedText);set('ecoText',ecoText);set('irr',turb>38?'WATCH':'GOOD');set('bTurb',bTurb);set('bSed',bSed);set('bPol',bPol);set('bIrr',bIrr);set('abr',turbRisk.toFixed(0));set('silt',silt.toFixed(0));set('corrRisk',cor.toFixed(0));width('abrBar',turbRisk);width('siltBar',silt);width('corrBar',cor)}update();setInterval(update,2000);
</script></body></html>
"""
        water_html = (water_html
            .replace('__PH__', f"{data['ph']:.2f}")
            .replace('__TURB__', f"{data['turbidity']:.1f}")
            .replace('__DO__', f"{data['do']:.1f}")
            .replace('__EC__', f"{data['conductivity']:.0f}")
            .replace('__TEMP__', f"{data['water_temp']:.1f}")
        )
        components.html(water_html, height=995, scrolling=False)

    elif page == "🏛️ Dam Intelligence":
        dam_html = """
<!DOCTYPE html><html><head><style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
*{box-sizing:border-box}body{margin:0;background:transparent;color:#eef7ff;font-family:Inter,Arial,sans-serif;overflow:hidden}.wrap{padding:0 0 8px 0}.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:18px}.kpi{min-height:132px;border:1px solid rgba(94,234,212,.23);border-radius:24px;padding:18px 20px;background:linear-gradient(155deg,rgba(8,61,48,.82),rgba(3,24,33,.72));box-shadow:0 18px 44px rgba(0,0,0,.23),inset 0 1px 0 rgba(255,255,255,.045);position:relative;overflow:hidden}.kpi:before{content:"";position:absolute;right:-36px;top:-40px;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.25),transparent 70%)}.kl{font-size:12px;color:#a7cfc4;font-weight:900;letter-spacing:1px;text-transform:uppercase}.kv{font-size:32px;font-weight:950;letter-spacing:-1px;margin-top:16px;color:#f2fff9}.ku{font-size:16px;color:#a8d4cc;margin-left:4px;font-weight:800}.kn{font-size:12px;color:#b7d2cc;margin-top:12px}.spark{height:2px;margin-top:16px;border-radius:99px;background:linear-gradient(90deg,rgba(94,234,212,.06),rgba(94,234,212,.88),rgba(255,209,102,.30),rgba(94,234,212,.06));background-size:240% 100%;animation:spark 2.2s linear infinite}@keyframes spark{from{background-position:0 0}to{background-position:240% 0}}.grid{display:grid;grid-template-columns:1.42fr .98fr;gap:18px}.panel{border:1px solid rgba(94,234,212,.20);border-radius:26px;background:linear-gradient(160deg,rgba(4,47,39,.76),rgba(2,17,27,.72));box-shadow:0 22px 58px rgba(0,0,0,.25);position:relative;overflow:hidden}.hero{height:684px;padding:28px 32px;background:radial-gradient(circle at 18% 15%,rgba(94,234,212,.14),transparent 28%),radial-gradient(circle at 64% 54%,rgba(255,209,102,.12),transparent 34%),linear-gradient(160deg,rgba(5,50,43,.82),rgba(2,17,27,.74))}.hero:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(45deg,rgba(94,234,212,.04) 0 1px,transparent 1px 62px),repeating-linear-gradient(-45deg,rgba(94,234,212,.03) 0 1px,transparent 1px 62px)}.title{position:relative;z-index:4;font-size:25px;font-weight:950;letter-spacing:-.5px;color:#f2fff9}.sub{position:relative;z-index:4;font-size:13px;color:#b7d2cc;margin-top:8px;max-width:810px;line-height:1.45}.stage{position:absolute;inset:104px 22px 18px 22px;z-index:3}.damcut{position:absolute;left:52px;top:78px;width:360px;height:455px;border-radius:28px;background:linear-gradient(180deg,rgba(36,211,238,.28) 0 32%,rgba(7,31,50,.70) 33% 100%);border:1px solid rgba(94,234,212,.22);box-shadow:inset 0 0 65px rgba(94,234,212,.08),0 20px 48px rgba(0,0,0,.24);overflow:hidden}.water{position:absolute;left:-20%;right:-20%;top:130px;height:20px;border-radius:50%;background:linear-gradient(90deg,rgba(127,255,212,.12),rgba(94,234,212,.78),rgba(127,255,212,.12));animation:wave 3.2s ease-in-out infinite}.body{position:absolute;left:95px;top:120px;width:160px;height:300px;background:linear-gradient(90deg,rgba(183,204,216,.75),rgba(232,243,248,.82),rgba(140,160,176,.72));clip-path:polygon(32% 0,68% 0,100% 100%,0 100%);box-shadow:0 0 30px rgba(255,255,255,.18)}.seep{position:absolute;left:245px;top:238px;width:120px;height:42px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.50),transparent 65%);filter:blur(1px);animation:seep 2.6s ease-in-out infinite}.sensor{position:absolute;border:1px solid rgba(94,234,212,.24);background:rgba(2,18,26,.72);border-radius:15px;padding:8px 10px;box-shadow:0 12px 24px rgba(0,0,0,.32);backdrop-filter:blur(8px);font-size:11px}.sensor b{display:block;color:#eef7ff;font-size:12px}.sensor span{color:#a7cfc4}.pz{left:54px;top:164px}.sp{left:46px;top:294px}.tl{left:240px;top:371px}.jm{left:216px;top:96px}.dot{width:13px;height:13px;border-radius:50%;display:inline-block;margin-right:6px;background:#67e8a5;box-shadow:0 0 15px rgba(103,232,165,.95)}.dot.amber{background:#ffd166;box-shadow:0 0 15px rgba(255,209,102,.95)}.model{position:absolute;left:448px;top:44px;right:28px;height:330px;border:1px solid rgba(94,234,212,.24);border-radius:28px;background:linear-gradient(145deg,rgba(3,31,44,.76),rgba(2,18,26,.70));box-shadow:0 18px 42px rgba(0,0,0,.26);padding:24px}.model-title{font-size:12px;color:#8ffff0;font-weight:950;letter-spacing:.9px;text-transform:uppercase}.hub{position:absolute;left:50%;top:49%;width:158px;height:158px;margin-left:-79px;margin-top:-79px;border-radius:50%;background:radial-gradient(circle at 38% 30%,rgba(255,209,102,.30),rgba(10,45,61,.92) 60%,rgba(3,16,24,.96));border:2px solid rgba(255,209,102,.52);display:flex;align-items:center;justify-content:center;text-align:center;font-weight:950;color:#ffd166;box-shadow:0 0 36px rgba(255,209,102,.20);animation:hubPulse 2.7s ease-in-out infinite}.hub small{display:block;color:#fff;font-size:10px;margin-top:5px}.node{position:absolute;width:124px;height:58px;border:1px solid rgba(94,234,212,.22);border-radius:18px;background:rgba(255,255,255,.045);display:flex;align-items:center;justify-content:center;text-align:center;color:#dffbf1;font-size:12px;font-weight:850}.n1{left:24px;top:72px}.n2{left:24px;bottom:58px}.n3{right:22px;top:72px}.n4{right:22px;bottom:58px}.n5{left:50%;margin-left:-62px;top:26px}.n6{left:50%;margin-left:-62px;bottom:24px}.beam{position:absolute;height:4px;border-radius:99px;background:linear-gradient(90deg,transparent,#34d399,#5eead4,#ffd166,transparent);background-size:220% 100%;animation:beam 1.9s linear infinite;box-shadow:0 0 18px rgba(94,234,212,.35);transform-origin:left center}.b1{left:146px;top:105px;width:150px;transform:rotate(20deg)}.b2{left:146px;bottom:90px;width:150px;transform:rotate(-20deg)}.b3{right:146px;top:105px;width:150px;transform:rotate(160deg)}.b4{right:146px;bottom:90px;width:150px;transform:rotate(-160deg)}.b5{left:50%;top:84px;width:120px;transform:rotate(90deg)}.b6{left:50%;bottom:84px;width:120px;transform:rotate(-90deg)}.decision{position:absolute;left:448px;right:28px;bottom:28px;border:1px solid rgba(94,234,212,.22);border-radius:24px;background:rgba(2,18,26,.76);padding:17px 18px}.decision b{color:#8ffff0;font-size:12px;text-transform:uppercase;letter-spacing:.8px}.decision .decrow{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:13px}.dec{border:1px solid rgba(94,234,212,.14);background:rgba(255,255,255,.04);border-radius:16px;padding:10px}.dec small{display:block;color:#a7cfc4;font-size:10px}.dec strong{display:block;color:#fff;margin-top:5px;font-size:14px}.side{min-height:684px;padding:22px}.pt{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}.pt h3{margin:0;font-size:18px;font-weight:950}.pt span{font-size:12px;color:#a7cfc4}.ai{border:1px solid rgba(94,234,212,.26);border-radius:22px;padding:17px 18px;background:linear-gradient(145deg,rgba(94,234,212,.12),rgba(8,21,38,.50));margin-bottom:14px}.bt{font-size:12px;color:#8ffff0;font-weight:950;letter-spacing:.9px;text-transform:uppercase;margin-bottom:10px}.big{font-size:35px;font-weight:950;color:#f2fff9;letter-spacing:-1px}.stat{font-size:13px;font-weight:950;color:#9dffc8;margin-left:8px}.txt{font-size:14px;color:#e8f7ff;line-height:1.58}.matrix{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 14px}.mx{border:1px solid rgba(94,234,212,.16);border-radius:18px;padding:12px;background:rgba(255,255,255,.04)}.mx small{display:block;color:#a7cfc4;font-size:11px}.mx b{display:block;margin-top:6px;color:#fff;font-size:15px}.meter{margin:13px 0}.mh{display:flex;justify-content:space-between;font-size:12px;color:#c7d9e9;margin-bottom:6px}.mb{height:10px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden}.mf{height:100%;border-radius:99px;background:linear-gradient(90deg,#34d399,#5eead4,#ffd166);transition:width .5s}.trigger{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:12px}.tr{border:1px solid rgba(94,234,212,.16);background:rgba(255,255,255,.04);border-radius:15px;padding:10px;font-size:11px;color:#dffbf1}.tr b{color:#ffd166}.bottom{margin-top:18px;padding:18px 20px}.bottom .chips{display:flex;gap:10px;flex-wrap:wrap}.bottom .chip{border:1px solid rgba(94,234,212,.20);border-radius:999px;background:rgba(255,255,255,.045);padding:10px 13px;color:#dffbf1;font-size:13px}.bottom .chip b{color:#8ffff0}@keyframes wave{0%,100%{transform:translateX(0) scaleY(1)}50%{transform:translateX(14px) scaleY(.82)}}@keyframes seep{0%,100%{transform:translate(0,0) scale(.9);opacity:.45}50%{transform:translate(18px,4px) scale(1.15);opacity:.95}}@keyframes hubPulse{0%,100%{box-shadow:0 0 24px rgba(255,209,102,.14)}50%{box-shadow:0 0 48px rgba(255,209,102,.32)}}@keyframes beam{from{background-position:0 0}to{background-position:220% 0}}
</style></head><body><div class="wrap"><div class="kpis"><div class="kpi"><div class="kl">STRUCTURAL RISK INDEX</div><div class="kv"><span id="riskIdx">__RISK__</span><span class="ku">%</span></div><div class="kn"><span id="riskNote">LOW • stable dam behaviour</span></div><div class="spark"></div></div><div class="kpi"><div class="kl">PORE PRESSURE</div><div class="kv"><span id="pzK">__PZ__</span><span class="ku">kPa</span></div><div class="kn">Rainfall-driven watch variable</div><div class="spark"></div></div><div class="kpi"><div class="kl">SEEPAGE RESPONSE</div><div class="kv"><span id="seepK">__SEEP__</span><span class="ku">L/min</span></div><div class="kn"><span id="seepNote">Baseline stable</span></div><div class="spark"></div></div><div class="kpi"><div class="kl">RECOMMENDED DECISION</div><div class="kv"><span id="decisionTop">NORMAL</span></div><div class="kn">No gate restriction</div><div class="spark"></div></div></div><div class="grid"><div class="panel hero"><div class="title">Dam Structural Intelligence & Decision Support</div><div class="sub">Piezometer, seepage, deformation, tilt, joint meter, rainfall and reservoir loading are fused into one structural risk model and decision recommendation.</div><div class="stage"><div class="damcut"><div class="water"></div><div class="body"></div><div class="seep"></div><div class="sensor pz"><span class="dot"></span><b>PZ-07</b><span><span id="pzS">__PZ__</span> kPa</span></div><div class="sensor sp"><span class="dot amber"></span><b>SP-04</b><span><span id="spS">__SEEP__</span> L/min</span></div><div class="sensor tl"><span class="dot"></span><b>TL-01</b><span><span id="tiltS">0.18</span>°</span></div><div class="sensor jm"><span class="dot"></span><b>JM-02</b><span><span id="jointS">0.44</span> mm</span></div></div><div class="model"><div class="model-title">Structural Reasoning Model</div><div class="node n1">Reservoir<br>Loading</div><div class="node n2">Rainfall<br>Persistence</div><div class="node n3">Pore Pressure<br>Response</div><div class="node n4">Seepage +<br>Deformation</div><div class="node n5">Tilt / Joint<br>Movement</div><div class="node n6">Temperature<br>Context</div><div class="beam b1"></div><div class="beam b2"></div><div class="beam b3"></div><div class="beam b4"></div><div class="beam b5"></div><div class="beam b6"></div><div class="hub">DAM STRESS<br><small>fusion engine</small></div></div><div class="decision"><b>Decision Logic Output</b><div class="decrow"><div class="dec"><small>Current Condition</small><strong id="cond">STABLE</strong></div><div class="dec"><small>Watch Item</small><strong id="watch">PZ-07 Trend</strong></div><div class="dec"><small>Action</small><strong id="action">Normal Operation</strong></div></div></div></div></div><div class="panel side"><div class="pt"><h3>Dam Intelligence Interpretation</h3><span>risk • scenario • decision</span></div><div class="ai"><div class="bt">AI Dam Safety Advisor</div><div class="txt"><div><span class="big" id="state">STABLE</span><span class="stat" id="stateStat">LOW RISK</span></div><span id="aiText">Dam behaviour remains stable. Mild pore-pressure increase is consistent with rainfall response and is not supported by seepage or deformation escalation.</span></div></div><div class="matrix"><div class="mx"><small>Hydraulic Pressure Stability</small><b id="mPz">Normal Watch</b></div><div class="mx"><small>Seepage Baseline</small><b id="mSeep">Stable</b></div><div class="mx"><small>Deformation Stability</small><b id="mDef">Stable</b></div><div class="mx"><small>Reservoir Loading</small><b id="mLoad">Normal Zone</b></div></div><div class="bt">Structural Health Components</div><div class="meter"><div class="mh"><span>Pressure Stability</span><b><span id="barPz">92</span>%</b></div><div class="mb"><div class="mf" id="barPzW" style="width:92%"></div></div></div><div class="meter"><div class="mh"><span>Seepage Consistency</span><b><span id="barSeep">96</span>%</b></div><div class="mb"><div class="mf" id="barSeepW" style="width:96%"></div></div></div><div class="meter"><div class="mh"><span>Deformation Stability</span><b><span id="barDef">98</span>%</b></div><div class="mb"><div class="mf" id="barDefW" style="width:98%"></div></div></div><div class="ai"><div class="bt">Trigger Matrix</div><div class="trigger"><div class="tr"><b>WATCH</b><br>Pore pressure ↑ + seepage stable</div><div class="tr"><b>INSPECT</b><br>Pore pressure ↑ + seepage ↑</div><div class="tr"><b>ALERT</b><br>Seepage ↑ + deformation ↑</div><div class="tr"><b>CRITICAL</b><br>Deformation ↑ + tilt ↑</div></div></div><div class="ai"><div class="bt">6–12 Hour Scenario</div><div class="txt" id="scenario">Risk remains low if rainfall does not intensify. Pore pressure may increase slightly without expected deformation response.</div></div></div></div><div class="panel bottom"><div class="pt"><h3>Decision Support Summary</h3><span>structural data translated into action</span></div><div class="chips"><div class="chip"><b>Gate Operation:</b> <span id="bGate">no restriction</span></div><div class="chip"><b>Inspection:</b> <span id="bInspect">not required</span></div><div class="chip"><b>Monitoring:</b> <span id="bMonitor">2-hour normal watch</span></div><div class="chip"><b>Escalation:</b> <span id="bEsc">only if seepage and deformation rise together</span></div></div></div></div><script>
const $=id=>document.getElementById(id);function clamp(v,a,b){return Math.max(a,Math.min(b,v))}function wave(b,a,p,ph=0){return b+a*Math.sin((Date.now()/1000+ph)/p)}function set(id,val){const e=$(id);if(e)e.textContent=val}function width(id,val){const e=$(id);if(e)e.style.width=val+'%'}
function update(){let pz=clamp(wave(__PZ__,2.6,6,1),136,151),seep=clamp(wave(__SEEP__,1.1,7,2),16.8,22.5),def=clamp(wave(__DEF__,.13,8,1),1.55,2.18),tilt=clamp(wave(.18,.025,7,2),.12,.24),joint=clamp(wave(.44,.035,8,3),.35,.54),rain=clamp(wave(__RAIN__,4.5,9,1),4,22);let pzScore=clamp(100-(pz-135)*.85,82,98),seepScore=clamp(100-(seep-15)*1.35,82,99),defScore=clamp(100-def*2.2,90,99),risk=clamp(100-((pzScore*.36)+(seepScore*.34)+(defScore*.30)),2,18);let state='STABLE',stat='LOW RISK',decision='NORMAL',cond='STABLE',watch='PZ-07 Trend',action='Normal Operation',riskNote='LOW • stable dam behaviour',seepNote='Baseline stable',ai=`Dam behaviour remains stable. Pore pressure at ${pz.toFixed(1)} kPa is consistent with rainfall response and is not supported by seepage or deformation escalation.`,scenario='Risk remains LOW if rainfall does not intensify. Pore pressure may increase +2–4 kPa with no expected deformation response.',inspect='not required',monitor='2-hour normal watch',esc='only if seepage and deformation rise together';let mPz='Normal Watch',mSeep='Stable',mDef='Stable',mLoad='Normal Zone';if(pz>146||rain>16){stat='WATCH';decision='WATCH';watch='Rainfall + PZ-07';riskNote='WATCH • rainfall response';mPz='Rainfall Response';ai=`PZ-07 is trending upward while seepage and deformation remain stable. This indicates hydraulic response to rainfall, not structural distress. Increase watch frequency if rainfall persists.`;scenario='Next 6–12 hours: pore pressure may rise moderately. Escalate only if seepage also increases or deformation trend appears.';monitor='hourly watch if rain persists';}if(seep>21&&pz>146){state='INSPECT';stat='MEDIUM RISK';decision='INSPECT';cond='HYDRAULIC WATCH';action='Field Verification';mSeep='Increasing';riskNote='MEDIUM • inspect seepage';seepNote='Increasing response';ai=`Combined pore pressure and seepage increase detected. Recommend field verification of seepage point SP-04 and review rainfall-reservoir loading correlation before changing gate strategy.`;scenario='If seepage continues upward over the next 6 hours, inspection priority increases. Gate operation may remain normal unless deformation also rises.';inspect='field verification';monitor='hourly structural watch';esc='if deformation / tilt rises';}if(def>2.05&&seep>21){state='ALERT';stat='HIGH RISK';decision='ALERT';cond='STRUCTURAL ALERT';action='Engineering Review';mDef='Movement Watch';riskNote='HIGH • engineering review';ai=`Seepage increase is accompanied by deformation trend. Engineering review is required and emergency response readiness should be checked.`;scenario='Potential coupled hydraulic-structural response. Prepare escalation if tilt and joint movement continue rising.';inspect='urgent inspection';monitor='continuous watch';esc='activate dam safety protocol';}
set('pzK',pz.toFixed(1));set('pzS',pz.toFixed(1));set('seepK',seep.toFixed(1));set('spS',seep.toFixed(1));set('tiltS',tilt.toFixed(2));set('jointS',joint.toFixed(2));set('riskIdx',risk.toFixed(1));set('riskNote',riskNote);set('seepNote',seepNote);set('decisionTop',decision);set('state',state);set('stateStat',stat);set('aiText',ai);set('cond',cond);set('watch',watch);set('action',action);set('mPz',mPz);set('mSeep',mSeep);set('mDef',mDef);set('mLoad',mLoad);set('scenario',scenario);set('bInspect',inspect);set('bMonitor',monitor);set('bEsc',esc);set('barPz',pzScore.toFixed(0));set('barSeep',seepScore.toFixed(0));set('barDef',defScore.toFixed(0));width('barPzW',pzScore);width('barSeepW',seepScore);width('barDefW',defScore)}update();setInterval(update,2000);
</script></body></html>
"""
        dam_html = (dam_html
            .replace('__PZ__', f"{data['piezometer']:.1f}")
            .replace('__SEEP__', f"{data['seepage']:.1f}")
            .replace('__DEF__', f"{live(1.8,.2,27,.03):.2f}")
            .replace('__RAIN__', f"{data['rainfall']:.1f}")
            .replace('__RISK__', f"{max(2.5, 100-data['dam_health']):.1f}")
        )
        components.html(dam_html, height=1015, scrolling=False)

    elif page == "🌊 Reservoir & Hydrology":
        res_html = """
<!DOCTYPE html><html><head><style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
*{box-sizing:border-box}body{margin:0;background:transparent;color:#eef7ff;font-family:Inter,Arial,sans-serif;overflow:hidden}.wrap{padding:0 0 8px 0}.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:18px}.kpi{min-height:132px;border:1px solid rgba(94,234,212,.23);border-radius:24px;padding:18px 20px;background:linear-gradient(155deg,rgba(8,61,48,.82),rgba(3,24,33,.72));box-shadow:0 18px 44px rgba(0,0,0,.23),inset 0 1px 0 rgba(255,255,255,.045);position:relative;overflow:hidden}.kpi:before{content:"";position:absolute;right:-38px;top:-42px;width:126px;height:126px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.25),transparent 70%)}.kl{font-size:12px;color:#a7cfc4;font-weight:900;letter-spacing:1px;text-transform:uppercase}.kv{font-size:32px;font-weight:950;letter-spacing:-1px;margin-top:16px;color:#f2fff9}.ku{font-size:16px;color:#a8d4cc;margin-left:4px;font-weight:800}.kn{font-size:12px;color:#b7d2cc;margin-top:12px}.spark{height:2px;margin-top:16px;border-radius:99px;background:linear-gradient(90deg,rgba(94,234,212,.06),rgba(94,234,212,.88),rgba(255,209,102,.32),rgba(94,234,212,.06));background-size:240% 100%;animation:spark 2.2s linear infinite}@keyframes spark{from{background-position:0 0}to{background-position:240% 0}}
.grid{display:grid;grid-template-columns:1.44fr .96fr;gap:18px}.panel{border:1px solid rgba(94,234,212,.20);border-radius:26px;background:linear-gradient(160deg,rgba(4,47,39,.76),rgba(2,17,27,.72));box-shadow:0 22px 58px rgba(0,0,0,.25);position:relative;overflow:hidden}.hero{height:706px;padding:28px 30px;background:radial-gradient(circle at 18% 13%,rgba(94,234,212,.13),transparent 28%),radial-gradient(circle at 76% 58%,rgba(255,209,102,.11),transparent 34%),linear-gradient(160deg,rgba(5,50,43,.82),rgba(2,17,27,.74))}.hero:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(45deg,rgba(94,234,212,.035) 0 1px,transparent 1px 62px),repeating-linear-gradient(-45deg,rgba(94,234,212,.026) 0 1px,transparent 1px 62px)}.title{position:relative;z-index:4;font-size:25px;font-weight:950;letter-spacing:-.5px;color:#f2fff9}.sub{position:relative;z-index:4;font-size:13px;color:#b7d2cc;margin-top:8px;max-width:850px;line-height:1.45}.chart{position:absolute;left:34px;right:34px;top:112px;height:400px;border:1px solid rgba(94,234,212,.18);border-radius:28px;background:linear-gradient(180deg,rgba(5,26,41,.72),rgba(2,16,28,.78));box-shadow:inset 0 0 70px rgba(94,234,212,.07);overflow:hidden}.zone{position:absolute;left:0;right:0;border-bottom:1px dashed rgba(255,255,255,.12);font-size:11px;color:#a7cfc4;padding:6px 12px}.z1{top:0;height:74px;background:rgba(255,209,102,.09)}.z2{top:74px;height:92px;background:rgba(94,234,212,.08)}.z3{top:166px;height:116px;background:rgba(52,211,153,.06)}.z4{top:282px;height:70px;background:rgba(59,130,246,.06)}.z5{top:352px;height:48px;background:rgba(255,209,102,.08);color:#ffd166}.axis{position:absolute;left:70px;right:34px;top:38px;bottom:44px;border-left:1px solid rgba(255,255,255,.14);border-bottom:1px solid rgba(255,255,255,.14)}.curve{position:absolute;left:92px;right:50px;top:60px;height:270px}.line{position:absolute;height:4px;border-radius:99px;background:rgba(255,255,255,.35);transform-origin:left center;box-shadow:0 0 12px rgba(255,255,255,.10)}.planned{background:linear-gradient(90deg,#9ca3af,#d1d5db);opacity:.68}.actual{background:linear-gradient(90deg,#34d399,#5eead4,#8ffff0);height:5px;box-shadow:0 0 18px rgba(94,234,212,.55)}.forecast{background:linear-gradient(90deg,#ffd166,#fbbf24);height:4px;box-shadow:0 0 18px rgba(255,209,102,.45)}.dotnow{position:absolute;width:18px;height:18px;border-radius:50%;background:#67e8a5;box-shadow:0 0 0 8px rgba(103,232,165,.11),0 0 24px rgba(103,232,165,.85);left:55%;top:120px;z-index:4}.dotlabel{position:absolute;left:58%;top:96px;background:rgba(2,18,26,.80);border:1px solid rgba(94,234,212,.26);border-radius:14px;padding:9px 11px;font-size:12px;color:#dffbf1;box-shadow:0 12px 24px rgba(0,0,0,.32)}.dry{position:absolute;right:62px;top:62px;border:1px solid rgba(255,209,102,.32);background:rgba(255,209,102,.08);border-radius:16px;padding:10px 12px;font-size:12px;color:#ffe9a8;max-width:230px}.hydro{position:absolute;left:34px;right:34px;bottom:26px;display:grid;grid-template-columns:1.1fr .9fr .95fr;gap:14px}.hcard{border:1px solid rgba(94,234,212,.18);border-radius:22px;background:rgba(2,18,26,.66);padding:16px;min-height:142px}.hcard b{font-size:12px;color:#8ffff0;text-transform:uppercase;letter-spacing:.8px}.hcard p{font-size:13px;line-height:1.5;color:#dcefff;margin:10px 0 0}.hydrograph{height:76px;margin-top:12px;position:relative;border-bottom:1px solid rgba(255,255,255,.14);border-left:1px solid rgba(255,255,255,.14);overflow:hidden}.hgline{position:absolute;height:5px;border-radius:99px;background:linear-gradient(90deg,#34d399,#5eead4,#ffd166);box-shadow:0 0 15px rgba(94,234,212,.35);transform-origin:left center}.hg1{left:8px;bottom:12px;width:58px;transform:rotate(-16deg)}.hg2{left:62px;bottom:28px;width:65px;transform:rotate(-33deg)}.hg3{left:122px;bottom:61px;width:62px;transform:rotate(16deg)}.hg4{left:178px;bottom:49px;width:58px;transform:rotate(28deg)}.sedbar{height:11px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden;margin-top:10px}.sedfill{height:100%;border-radius:99px;background:linear-gradient(90deg,#34d399,#5eead4,#ffd166);width:38%;animation:sed 3s ease-in-out infinite}.side{min-height:706px;padding:22px}.pt{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}.pt h3{margin:0;font-size:18px;font-weight:950}.pt span{font-size:12px;color:#a7cfc4}.ai{border:1px solid rgba(94,234,212,.26);border-radius:22px;padding:17px 18px;background:linear-gradient(145deg,rgba(94,234,212,.12),rgba(8,21,38,.50));margin-bottom:14px}.bt{font-size:12px;color:#8ffff0;font-weight:950;letter-spacing:.9px;text-transform:uppercase;margin-bottom:10px}.big{font-size:34px;font-weight:950;color:#f2fff9;letter-spacing:-1px}.stat{font-size:13px;font-weight:950;color:#9dffc8;margin-left:8px}.txt{font-size:14px;color:#e8f7ff;line-height:1.58}.matrix{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 14px}.mx{border:1px solid rgba(94,234,212,.16);border-radius:18px;padding:12px;background:rgba(255,255,255,.04)}.mx small{display:block;color:#a7cfc4;font-size:11px}.mx b{display:block;margin-top:6px;color:#fff;font-size:15px}.meter{margin:13px 0}.mh{display:flex;justify-content:space-between;font-size:12px;color:#c7d9e9;margin-bottom:6px}.mb{height:10px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden}.mf{height:100%;border-radius:99px;background:linear-gradient(90deg,#34d399,#5eead4,#ffd166);transition:width .5s}.decision{border:1px solid rgba(255,209,102,.25);background:linear-gradient(145deg,rgba(255,209,102,.10),rgba(8,21,38,.50));border-radius:22px;padding:16px;margin-top:14px}.bottom{margin-top:18px;padding:18px 20px}.chips{display:flex;gap:10px;flex-wrap:wrap}.chip{border:1px solid rgba(94,234,212,.20);border-radius:999px;background:rgba(255,255,255,.045);padding:10px 13px;color:#dffbf1;font-size:13px}.chip b{color:#8ffff0}@keyframes sed{0%,100%{width:34%}50%{width:47%}}
</style></head><body><div class="wrap"><div class="kpis"><div class="kpi"><div class="kl">RULE CURVE POSITION</div><div class="kv"><span id="curvePos">+3.8</span><span class="ku">%</span></div><div class="kn">Actual storage above planned operation curve</div><div class="spark"></div></div><div class="kpi"><div class="kl">INFLOW FORECAST</div><div class="kv"><span id="inflowK">__INFLOW__</span><span class="ku">m³/s</span></div><div class="kn"><span id="inflowNote">Rising limb detected</span></div><div class="spark"></div></div><div class="kpi"><div class="kl">OPERATIONAL DRIFT</div><div class="kv"><span id="driftK">LOW</span></div><div class="kn">El Niño dry-drift scenario monitored</div><div class="spark"></div></div><div class="kpi"><div class="kl">RECOMMENDED MODE</div><div class="kv"><span id="modeK">NORMAL</span></div><div class="kn">Maintain dispatch • no spillway release</div><div class="spark"></div></div></div><div class="grid"><div class="panel hero"><div class="title">Reservoir & Hydrology Intelligence</div><div class="sub">Operating rule curve, rainfall, inflow forecast, upstream flood hydrograph, El Niño drift scenario, and sediment/dead-storage watch fused into one reservoir decision view.</div><div class="chart"><div class="zone z1">Flood Control Zone</div><div class="zone z2">Upper Rule Curve / High Conservation</div><div class="zone z3">Normal Operation Zone</div><div class="zone z4">Conservation Zone</div><div class="zone z5">Dead Storage / Sediment Reserve</div><div class="axis"><div class="curve"><div class="line planned" style="left:0;top:135px;width:165px;transform:rotate(-5deg)"></div><div class="line planned" style="left:160px;top:121px;width:170px;transform:rotate(7deg)"></div><div class="line planned" style="left:324px;top:143px;width:170px;transform:rotate(3deg)"></div><div class="line actual" style="left:0;top:112px;width:168px;transform:rotate(-10deg)"></div><div class="line actual" style="left:162px;top:83px;width:168px;transform:rotate(8deg)"></div><div class="line forecast" style="left:325px;top:105px;width:188px;transform:rotate(14deg)"></div><div class="dotnow"></div><div class="dotlabel"><b>Current Storage</b><br><span id="storageTxt">__STORAGE__%</span> • EL <span id="levelTxt">__LEVEL__</span> m</div></div></div><div class="dry"><b>Scenario Watch</b><br>El Niño may shift dry-season reservoir trajectory below planned curve if inflow deficit persists.</div></div><div class="hydro"><div class="hcard"><b>Upstream Hydrograph</b><p id="hydroText">Rising limb detected. Estimated flood-wave peak arrival 4–6 hours; flood routing risk remains low to moderate.</p><div class="hydrograph"><div class="hgline hg1"></div><div class="hgline hg2"></div><div class="hgline hg3"></div><div class="hgline hg4"></div></div></div><div class="hcard"><b>Sedimentation / Dead Storage</b><p id="sedText">Turbidity indicates moderate sediment transport. Dead-storage impact remains low; verify bathymetry only if turbidity persists after flood pulse.</p><div class="sedbar"><div class="sedfill" id="sedFill"></div></div></div><div class="hcard"><b>Weather → Reservoir Driver</b><p id="weatherText">Rainfall and catchment response currently support positive inflow. Reservoir remains inside normal operating band.</p></div></div></div><div class="panel side"><div class="pt"><h3>Hydrology Interpretation</h3><span>plan • actual • forecast</span></div><div class="ai"><div class="bt">AI Reservoir Advisor</div><div class="txt"><div><span class="big" id="state">ON CURVE</span><span class="stat" id="stateStat">NORMAL</span></div><span id="aiText">Reservoir storage is above planned operation curve but still inside the normal operating band. Current inflow supports generation while spillway remains closed.</span></div></div><div class="matrix"><div class="mx"><small>Actual vs Plan</small><b id="mPlan">+3.8% above curve</b></div><div class="mx"><small>Flood Routing</small><b id="mFlood">Low / watch rising limb</b></div><div class="mx"><small>Dry-Season Drift</small><b id="mDry">El Niño scenario watch</b></div><div class="mx"><small>Sediment Storage</small><b id="mSed">Dead storage impact low</b></div></div><div class="bt">Hydrology Indices</div><div class="meter"><div class="mh"><span>Storage Reliability</span><b><span id="barStor">92</span>%</b></div><div class="mb"><div class="mf" id="barStorW" style="width:92%"></div></div></div><div class="meter"><div class="mh"><span>Flood Buffer</span><b><span id="barFlood">86</span>%</b></div><div class="mb"><div class="mf" id="barFloodW" style="width:86%"></div></div></div><div class="meter"><div class="mh"><span>Sediment Watch</span><b><span id="barSed">38</span>%</b></div><div class="mb"><div class="mf" id="barSedW" style="width:38%"></div></div></div><div class="decision"><div class="bt">Recommended Reservoir Decision</div><div class="txt" id="decisionText"><b>NORMAL DISPATCH.</b> Keep spillway closed, maintain turbine release, watch upstream hydrograph, and review release plan if inflow peak exceeds forecast.</div></div></div></div><div class="panel bottom"><div class="pt"><h3>Operational Consequence</h3><span>hydrology translated into reservoir operation</span></div><div class="chips"><div class="chip"><b>Dispatch:</b> <span id="bDispatch">maintain current generation</span></div><div class="chip"><b>Spillway:</b> <span id="bSpill">closed / standby</span></div><div class="chip"><b>Flood Hydrograph:</b> <span id="bHydro">rising limb, peak 4–6h</span></div><div class="chip"><b>Dry Drift:</b> <span id="bDry">monitor El Niño deficit scenario</span></div><div class="chip"><b>Sediment:</b> <span id="bSed">dead storage impact low</span></div></div></div></div><script>
const $=id=>document.getElementById(id);function clamp(v,a,b){return Math.max(a,Math.min(b,v))}function wave(b,a,p,ph=0){return b+a*Math.sin((Date.now()/1000+ph)/p)}function set(id,val){const e=$(id);if(e)e.textContent=val}function width(id,val){const e=$(id);if(e)e.style.width=val+'%'}
function update(){let level=clamp(wave(__LEVEL__,.22,7,1),325.9,327.1),storage=clamp(wave(__STORAGE__,1.3,8,2),79.4,86.8),inflow=clamp(wave(__INFLOW__,78,7,1),650,1040),outflow=clamp(wave(__OUTFLOW__,45,9,3),610,820),rain=clamp(wave(__RAIN__,4.8,8,2),4,24),turb=clamp(wave(__TURB__,5.5,6,1),12,38);let net=inflow-outflow,plan=clamp(storage-78.9,1.2,6.8),floodBuf=clamp(100-(storage-80)*4.2,58,94),storRel=clamp(88+plan*1.2,88,97),sed=clamp(turb*1.55,18,68);let mode='NORMAL',state='ON CURVE',stat='NORMAL',mFlood='Low / watch rising limb',decision='<b>NORMAL DISPATCH.</b> Keep spillway closed, maintain turbine release, watch upstream hydrograph, and review release plan if inflow peak exceeds forecast.',hydro='Rising limb detected. Estimated flood-wave peak arrival 4–6 hours; flood routing risk remains low to moderate.',ai=`Reservoir storage is ${plan.toFixed(1)}% above planned operation curve and still inside the normal operating band. Inflow is ${inflow.toFixed(0)} m³/s with net balance ${net.toFixed(0)} m³/s, supporting stable generation.`,spill='closed / standby',dispatch='maintain current generation';if(rain>18||inflow>960){state='HYDRO WATCH';stat='RISING INFLOW';mode='WATCH';mFlood='Moderate / route flood pulse';decision='<b>HYDRO WATCH.</b> Maintain generation release, keep spillway standby, and review routing if upstream peak exceeds forecast or storage approaches upper rule curve.';hydro='Rising limb is strengthening. Estimated peak arrival 3–5 hours; prepare flood routing review while maintaining normal turbine release.';spill='standby / review rule curve'}if(storage>85.2&&inflow>940){state='UPPER CURVE WATCH';stat='OPERATOR REVIEW';mode='REVIEW';mFlood='Moderate / upper curve watch';decision='<b>OPERATOR REVIEW.</b> Re-evaluate release plan against upper rule curve. Spillway remains closed unless storage crosses operating boundary.';spill='prepare controlled release review'}let dry='El Niño scenario watch',dryChip='monitor El Niño deficit scenario';if(rain<7&&inflow<720){dry='Dry drift risk increasing';dryChip='possible dry-season deficit';ai=`Inflow is weakening while rainfall is low. Reservoir remains operational, but El Niño dry-drift scenario may pull actual trajectory below planned curve if deficit persists.`}let sedText='Turbidity indicates moderate sediment transport. Dead-storage impact remains low; verify bathymetry only if turbidity persists after flood pulse.',sedLabel='Dead storage impact low',sedChip='dead storage impact low';if(turb>30){sedText='Elevated turbidity suggests stronger sediment influx from upstream runoff. Watch deltaic deposition and dead-storage accumulation; schedule bathymetry verification if repeated after flood events.';sedLabel='Sediment deposition watch';sedChip='sediment deposition watch'}set('curvePos','+'+plan.toFixed(1));set('inflowK',inflow.toFixed(0));set('storageTxt',storage.toFixed(1)+'%');set('levelTxt',level.toFixed(2));set('inflowNote',inflow>900?'Rising limb strengthening':'Rising limb detected');set('driftK',dry.includes('increasing')?'WATCH':'LOW');set('modeK',mode);set('state',state);set('stateStat',stat);set('aiText',ai);set('mPlan','+'+plan.toFixed(1)+'% above curve');set('mFlood',mFlood);set('mDry',dry);set('mSed',sedLabel);set('decisionText',decision);set('hydroText',hydro);set('sedText',sedText);set('weatherText',`Rainfall ${rain.toFixed(1)} mm/h drives catchment response and inflow ${inflow.toFixed(0)} m³/s. Reservoir remains inside operating band.`);set('bDispatch',dispatch);set('bSpill',spill);set('bHydro',inflow>960?'strong rising limb, peak 3–5h':'rising limb, peak 4–6h');set('bDry',dryChip);set('bSed',sedChip);set('barStor',storRel.toFixed(0));set('barFlood',floodBuf.toFixed(0));set('barSed',sed.toFixed(0));width('barStorW',storRel);width('barFloodW',floodBuf);width('barSedW',sed);width('sedFill',sed)}update();setInterval(update,2000);
</script></body></html>
"""
        res_html = (res_html
            .replace('__LEVEL__', f"{data['reservoir_level']:.2f}")
            .replace('__STORAGE__', f"{data['reservoir_pct']:.1f}")
            .replace('__INFLOW__', f"{data['inflow']:.0f}")
            .replace('__OUTFLOW__', f"{data['outflow']:.0f}")
            .replace('__RAIN__', f"{data['rainfall']:.1f}")
            .replace('__TURB__', f"{data['turbidity']:.1f}")
        )
        components.html(res_html, height=1015, scrolling=False)

    elif page == "🌀 Powerhouse & Turbine":
        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("Turbine Health", f"{data['turbine_health']:.1f}", "%", "3 units online")
        with c2: kpi("RPM", f"{live(300,.7,13,.08):.1f}", "rpm", "Synchronized")
        with c3: kpi("Vibration U2", f"{data['vib']:.2f}", "mm/s", "Normal")
        with c4: kpi("Bearing Temp", f"{data['bearing_temp']:.1f}", "°C", "Below advisory limit")
        left,right = st.columns([1.7,1])
        with left:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Powerhouse Digital View", "Turbine • generator • cooling • oil")
            components.html(powerhouse_svg(), height=545, scrolling=False)
            st.markdown('</div>', unsafe_allow_html=True)
        with right:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Turbine Health Analytics", "Unit #1–#3")
            bar("Unit #1 Health", 97.2 + math.sin(t/22)*.4)
            bar("Unit #2 Health", data["turbine_health"]-1.2)
            bar("Unit #3 Health", 96.9 + math.sin(t/18)*.5)
            metric("Cavitation Risk", "LOW")
            metric("Oil Pressure", f"{live(5.4,.2,24,.02):.2f} bar")
            metric("Cooling Flow", f"{live(320,15,26,2):.0f} L/min")
            st.markdown('<div class="ai-box"><div class="ai-title">AI Maintenance Signal</div><div class="ai-text">Unit #2 vibration is normal but trending slightly upward. No immediate action needed; inspect during next planned maintenance window.</div></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    elif page == "⚡ Electrical & Switchyard":
        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("Electrical Health", f"{data['electrical_health']:.1f}", "%", "Generator & auxiliary normal")
        with c2: kpi("Frequency", f"{data['freq']:.2f}", "Hz", "Grid synchronized")
        with c3: kpi("Power Factor", f"{data['pf']:.3f}", "", "Excellent")
        with c4: kpi("Switchyard", f"{data['switchyard_health']:.1f}", "%", "Export line healthy")
        left,right = st.columns([1.65,1])
        with left:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Premium Single Line Diagram", "Generator • Transformer • Switchyard • Grid")
            st.markdown(electrical_svg(), unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with right:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Power Quality & Asset Health", "Smart panel philosophy upgraded")
            metric("Generator Voltage", "13.8 kV")
            metric("Transformer Oil Temp", f"{live(58.3,1.2,21,.1):.1f} °C")
            metric("Breaker CB-02 Count", "18 operations")
            metric("Surge Arrester Leakage", f"{live(.42,.04,19,.01):.2f} mA")
            metric("THD", "2.1%")
            st.markdown('<div class="ai-box"><div class="ai-title">AI Electrical Note</div><div class="ai-text">Grid export quality is stable. No voltage unbalance or harmonic anomaly detected. Transformer thermal margin remains sufficient.</div></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)


    elif page == "🔗 Correlation Intelligence":
        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("Correlation Score", f"{data['corr_score']:.1f}", "%", "Cause-effect engine active")
        with c2: kpi("Active Chain", "Rain → Inflow", "", "Hydrology driver detected")
        with c3: kpi("Decision Impact", "+24", "MW", "Dispatch opportunity")
        with c4: kpi("Risk Status", "Normal", "", "No coupled dam anomaly")
        components.html(operational_correlation_component(), height=880, scrolling=False)

    elif page == "🤖 AI Recommendation Center":
        op_score = 97.2 + math.sin(t/25)*.8
        gain = 2.6 + math.sin(t/21)*.3
        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("AI Operational Score", f"{op_score:.1f}", "/100", "Executive decision brief")
        with c2: kpi("Top Priority", "Dispatch", "", "Unit #2 optimization")
        with c3: kpi("Emerging Risks", "3", "items", "Hydrology • PZ-07 • Sediment")
        with c4: kpi("Expected Gain", f"+{gain:.1f}", "%", "Efficiency + production uplift")

        st.markdown('''<style>
        .rec-hero{border:1px solid rgba(94,234,212,.22);border-radius:26px;padding:18px;background:linear-gradient(150deg,rgba(6,45,40,.82),rgba(4,20,30,.78));box-shadow:0 24px 70px rgba(0,0,0,.24);position:relative;overflow:hidden;margin-bottom:14px;}
        .rec-hero:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 20% 5%,rgba(94,234,212,.16),transparent 30%),radial-gradient(circle at 85% 12%,rgba(255,209,102,.09),transparent 25%),repeating-linear-gradient(45deg,rgba(94,234,212,.035) 0 1px,transparent 1px 58px);pointer-events:none;}
        .rec-hero>*{position:relative;z-index:1}.rec-grid{display:grid;grid-template-columns:1.05fr 1.35fr .95fr;gap:14px}.rec-card2{border:1px solid rgba(94,234,212,.18);border-radius:22px;background:rgba(3,18,28,.54);padding:16px;box-shadow:inset 0 1px 0 rgba(255,255,255,.04)}
        .rec-label{font-size:12px;text-transform:uppercase;letter-spacing:.9px;color:#8fffd7;font-weight:900}.rec-score{font-size:56px;font-weight:950;line-height:.95;letter-spacing:-2px;margin:14px 0 6px}.rec-pill{display:inline-flex;align-items:center;gap:7px;border-radius:999px;padding:7px 10px;border:1px solid rgba(103,232,165,.42);background:rgba(16,185,129,.13);color:#b8ffd6;font-size:12px;font-weight:900}.rec-dot{width:8px;height:8px;border-radius:50%;background:#67e8a5;box-shadow:0 0 14px #67e8a5}.rec-row{display:grid;grid-template-columns:110px 1fr 42px;gap:9px;align-items:center;margin:11px 0;font-size:12px;color:#c7d9e9}.rec-track{height:9px;border-radius:999px;background:rgba(255,255,255,.08);overflow:hidden}.rec-fill{height:100%;border-radius:999px;background:linear-gradient(90deg,#34d399,#5eead4);box-shadow:0 0 16px rgba(94,234,212,.45)}.priority{background:linear-gradient(150deg,rgba(8,62,51,.78),rgba(9,29,38,.72));border-color:rgba(103,232,165,.35)}.priority-title{font-size:26px;font-weight:950;letter-spacing:-.7px;margin:8px 0;color:#ffffff}.rec-text{color:#cfe4f3;font-size:13px;line-height:1.48}.reason-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:12px 0}.reason{border:1px solid rgba(94,234,212,.14);border-radius:14px;padding:10px;background:rgba(255,255,255,.045)}.reason b{display:block;font-size:16px;color:#fff}.reason span{font-size:11px;color:#a7cfc4}.action-box{display:flex;justify-content:space-between;align-items:center;border:1px solid rgba(255,209,102,.35);border-radius:18px;padding:12px;margin-top:12px;background:rgba(255,209,102,.08)}.badge2{border-radius:999px;padding:6px 9px;font-size:11px;font-weight:950;border:1px solid #67e8a5;color:#b8ffd6;background:rgba(103,232,165,.08);white-space:nowrap}.badge2.warn{border-color:#ffd166;color:#ffd166;background:rgba(255,209,102,.08)}.badge2.info{border-color:#5eead4;color:#a7fff0;background:rgba(94,234,212,.08)}
        .recommend-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}.recommend-card{border:1px solid rgba(94,234,212,.17);border-radius:21px;padding:15px;background:linear-gradient(145deg,rgba(7,45,40,.68),rgba(5,18,28,.68));position:relative;overflow:hidden}.recommend-card:before{content:"";position:absolute;right:-35px;top:-35px;width:110px;height:110px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.13),transparent 70%)}.recommend-card>*{position:relative;z-index:1}.rec-head{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}.rec-title{font-size:17px;font-weight:950;color:#fff}.impact-line{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:12px}.impact{border-radius:13px;padding:9px;background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.07)}.impact span{display:block;color:#a7cfc4;font-size:10px;text-transform:uppercase;font-weight:900;letter-spacing:.5px}.impact b{display:block;margin-top:3px;color:#fff;font-size:13px}.decision-strip{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:14px}.decision{border:1px solid rgba(94,234,212,.14);border-radius:16px;padding:12px;background:rgba(255,255,255,.04)}.decision small{display:block;color:#a7cfc4;font-weight:800}.decision b{display:block;margin-top:5px;color:#fff;font-size:14px}
        </style>''', unsafe_allow_html=True)

        st.markdown(f'''
        <div class="rec-hero">
          <div class="rec-grid">
            <div class="rec-card2">
              <div class="rec-label">AI Executive Brief</div>
              <div class="rec-score">{op_score:.1f}</div>
              <div class="rec-pill"><span class="rec-dot"></span> CONTINUE CURRENT STRATEGY</div>
              <div style="height:12px"></div>
              <div class="rec-row"><span>Plant Safety</span><div class="rec-track"><div class="rec-fill" style="width:98%"></div></div><b>98</b></div>
              <div class="rec-row"><span>Generation</span><div class="rec-track"><div class="rec-fill" style="width:94%"></div></div><b>94</b></div>
              <div class="rec-row"><span>Hydrology</span><div class="rec-track"><div class="rec-fill" style="width:92%"></div></div><b>92</b></div>
              <div class="rec-row"><span>Asset Health</span><div class="rec-track"><div class="rec-fill" style="width:96%"></div></div><b>96</b></div>
              <div class="rec-row"><span>ESG</span><div class="rec-track"><div class="rec-fill" style="width:97%"></div></div><b>97</b></div>
            </div>
            <div class="rec-card2 priority">
              <div class="rec-label">Top Priority Recommendation</div>
              <div class="priority-title">Increase Unit #2 output by 3–5% during peak demand window</div>
              <div class="rec-text">AI correlates reservoir storage, inflow trend, rainfall forecast, turbine health, and grid condition. Current water balance supports generation optimization without entering flood-control constraint.</div>
              <div class="reason-grid">
                <div class="reason"><span>Reservoir</span><b>{data['reservoir_pct']:.1f}%</b></div>
                <div class="reason"><span>Inflow</span><b>{data['inflow']:.0f} m³/s</b></div>
                <div class="reason"><span>Dam Safety</span><b>Normal</b></div>
                <div class="reason"><span>Grid Export</span><b>Stable</b></div>
              </div>
              <div class="action-box"><div><b style="color:#ffd166">Expected Benefit</b><br><span style="color:#cfe4f3;font-size:13px">+{gain:.1f}% energy conversion, no additional structural risk</span></div><div class="badge2">Recommended</div></div>
            </div>
            <div style="display:grid;gap:10px">
              <div class="rec-card2"><div class="rec-label">Operational Risk</div><div class="rec-score" style="font-size:34px;margin:8px 0">LOW</div><div class="rec-text">No coupled anomaly across dam safety, water quality, turbine and grid.</div></div>
              <div class="rec-card2"><div class="rec-label">Forecast Horizon</div><div class="rec-score" style="font-size:34px;margin:8px 0">72h</div><div class="rec-text">Rainfall may increase inflow; reservoir remains inside rule curve.</div></div>
            </div>
          </div>
        </div>''', unsafe_allow_html=True)

        recs = [
            ("Hydrology & Reservoir Operation", "Maintain turbine release and keep spillway closed. Review dispatch if upstream hydrograph peak exceeds forecast envelope.", "Priority 1", "", "Normal Dispatch", "Inflow Peak", "Operation"),
            ("Dam Safety Watch", "PZ-07 remains inside normal band but rising slowly. Increase watch frequency only if rainfall persists above 10 mm/h for 48 hours.", "Watch", "warn", "No Restriction", "PZ + Seepage", "Civil Safety"),
            ("Sediment & Dead Storage", "Turbidity and rainfall correlation indicates moderate sediment transport. Schedule bathymetric verification if turbidity remains elevated after flood pulse.", "Emerging", "warn", "Survey Watch", "Turbidity Trend", "Hydrology"),
            ("Turbine Maintenance", "Unit #2 vibration is normal but shows mild upward drift. Inspect bearing alignment in the next planned maintenance window.", "Advisory", "info", "Plan Inspection", "Vibration Drift", "O&M"),
            ("Electrical & Grid Export", "Frequency, PF, THD, transformer thermal margin and breaker status remain stable. No intervention required for switchyard equipment.", "Normal", "", "No Action", "None", "Electrical"),
            ("📊 ESG & Reporting", "Water quality, air quality, renewable generation and CO₂ avoided are within executive reporting envelope. Include sediment watch as monthly note.", "Compliant", "", "Report Green", "Monthly KPI", "ESG"),
        ]
        st.markdown('<div class="recommend-grid">', unsafe_allow_html=True)
        for title, body, status, cls, decision, trigger, owner in recs:
            st.markdown(f'''<div class="recommend-card"><div class="rec-head"><div class="rec-title">{title}</div><div class="badge2 {cls}">{status}</div></div><div class="rec-text" style="margin-top:9px">{body}</div><div class="impact-line"><div class="impact"><span>Decision</span><b>{decision}</b></div><div class="impact"><span>Trigger</span><b>{trigger}</b></div><div class="impact"><span>Owner</span><b>{owner}</b></div></div></div>''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('''<div class="rec-hero" style="margin-top:14px"><div class="rec-label">AI Daily Operational Brief</div><div style="font-size:15px;line-height:1.62;color:#eef8ff;margin-top:8px">Reservoir remains inside the planned operating rule curve. Weather forecast indicates moderate rainfall over the next 48 hours, supporting stable inflow. Current water balance allows a slight generation increase without affecting flood control reserve. Dam safety instrumentation remains within baseline. Turbine Unit #2 shows early vibration drift but is not operationally critical. Overall operational risk is LOW.</div><div class="decision-strip"><div class="decision"><small>Reservoir</small><b>Inside Rule Curve</b></div><div class="decision"><small>Spillway</small><b>Keep Closed</b></div><div class="decision"><small>Generation</small><b>Optimize Unit #2</b></div><div class="decision"><small>Dam Safety</small><b>Normal Watch</b></div><div class="decision"><small>Next Review</small><b>2 Hours</b></div></div></div>''', unsafe_allow_html=True)


    elif page == "🛠️ Predictive O&M Value":
        # Predictive O&M is the operational action layer: analytics from turbine, dam, hydrology,
        # electrical, and correlation pages are translated into work orders, timing, risk and value.
        unit2_vib = data['vib']
        bearing_temp = data['bearing_temp']
        reservoir_pct = data['reservoir_pct']
        inflow = data['inflow']
        generation = data['generation']
        freq = data['freq']
        pf = data['pf']

        hydro_window = "GOOD" if reservoir_pct > 78 and inflow > 760 else "LIMITED"
        grid_window = "STABLE" if 49.92 <= freq <= 50.08 and pf > 0.975 else "WATCH"
        unit2_priority = "MEDIUM" if unit2_vib < 2.6 and bearing_temp < 68 else "HIGH"
        downtime_hours = 3 if unit2_priority == "MEDIUM" else 6
        if_ignored_hours = 36 if unit2_priority == "MEDIUM" else 72
        financial_exposure = 38000 if unit2_priority == "MEDIUM" else 91000
        lost_gwh = 2.8 if unit2_priority == "MEDIUM" else 5.4
        confidence = min(98.5, 91 + (reservoir_pct-78)*0.45 + (pf-0.97)*80)

        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("Maintenance Priority", "Unit #2", "", f"{unit2_priority} • turbine train")
        with c2: kpi("Best Window", "Next", "24h", f"Hydrology {hydro_window} • Grid {grid_window}")
        with c3: kpi("Avoided Outage", f"{if_ignored_hours}", "h", "If vibration drift is ignored")
        with c4: kpi("Value Exposure", f"${financial_exposure/1000:.0f}k", "", "Preventive action value")

        st.markdown(f'''
        <style>
        .om-hero{{border:1px solid rgba(94,234,212,.24);background:linear-gradient(135deg,rgba(7,58,48,.82),rgba(4,20,30,.76));border-radius:28px;padding:20px;box-shadow:0 24px 70px rgba(0,0,0,.28);position:relative;overflow:hidden;margin-bottom:14px}}
        .om-hero:before{{content:"";position:absolute;right:-90px;top:-120px;width:360px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.18),transparent 68%);}}
        .om-title{{font-size:26px;font-weight:900;letter-spacing:-.6px;color:#f2fff9;margin-bottom:7px}}
        .om-sub{{font-size:13px;color:#a7cfc4;line-height:1.5;max-width:920px}}
        .om-grid{{display:grid;grid-template-columns:1.12fr .88fr;gap:14px;margin-top:14px}}
        .om-card{{border:1px solid rgba(94,234,212,.18);background:linear-gradient(150deg,rgba(255,255,255,.055),rgba(4,18,28,.35));border-radius:22px;padding:16px;position:relative;overflow:hidden}}
        .om-card.gold{{border-color:rgba(255,209,102,.35);background:linear-gradient(150deg,rgba(255,209,102,.12),rgba(4,18,28,.40));}}
        .om-label{{font-size:12px;color:#7fffd4;font-weight:900;text-transform:uppercase;letter-spacing:.9px}}
        .om-big{{font-size:38px;font-weight:900;color:#f2fff9;line-height:1;margin-top:8px;letter-spacing:-1.2px}}
        .om-badge{{display:inline-flex;padding:7px 10px;border-radius:999px;border:1px solid rgba(103,232,165,.30);background:rgba(103,232,165,.10);color:#b8ffd6;font-size:11px;font-weight:900;margin-left:8px}}
        .om-badge.warn{{border-color:rgba(255,209,102,.42);background:rgba(255,209,102,.10);color:#ffd166}}
        .evidence{{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin-top:14px}}
        .ev{{border:1px solid rgba(94,234,212,.12);border-radius:16px;padding:11px;background:rgba(255,255,255,.04)}}
        .ev small{{display:block;color:#a7cfc4;font-size:11px;margin-bottom:5px}}.ev b{{font-size:14px;color:#fff}}
        .workorder{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:12px}}
        .wo{{border:1px solid rgba(94,234,212,.13);border-radius:16px;padding:11px;background:rgba(255,255,255,.045)}}
        .wo small{{display:block;color:#a7cfc4;font-size:11px;margin-bottom:6px}}.wo b{{font-size:13px;color:#f2fff9}}
        .timeline2{{position:relative;margin-top:12px;padding-left:20px;border-left:2px solid rgba(94,234,212,.30)}}
        .tl2{{margin:0 0 12px 0;padding:11px 13px;border-radius:16px;background:rgba(255,255,255,.045);border:1px solid rgba(94,234,212,.12)}}
        .tl2 b{{color:#f2fff9}}.tl2 span{{display:block;color:#a9bfd3;font-size:12px;margin-top:4px;line-height:1.45}}
        .valuebar{{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center;margin:10px 0;color:#dffbf1}}
        .barbg{{height:8px;border-radius:99px;background:rgba(255,255,255,.09);overflow:hidden}}.barfill{{height:8px;border-radius:99px;background:linear-gradient(90deg,#5eead4,#67e8a5)}}
        .matrix2{{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-top:12px}}
        .mx2{{border:1px solid rgba(94,234,212,.14);border-radius:16px;padding:12px;background:rgba(255,255,255,.045)}}
        .mx2 small{{display:block;color:#a7cfc4;font-size:11px;margin-bottom:5px}}.mx2 b{{font-size:13px;color:#fff}}
        .action-strip{{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:14px}}
        .act{{border:1px solid rgba(94,234,212,.15);background:rgba(3,20,28,.48);border-radius:18px;padding:12px;text-align:center}}
        .act small{{display:block;color:#a7cfc4;font-size:11px;margin-bottom:6px}}.act b{{font-size:13px;color:#f2fff9}}
        </style>
        <div class="om-hero">
          <div class="om-title">Predictive O&M Value Center</div>
          <div class="om-sub">This page converts analytics from turbine vibration, bearing temperature, hydrology window, dam safety watch, and grid condition into a concrete maintenance action: what to do, when to do it, who owns it, why now, and what value is protected.</div>
          <div class="om-grid">
            <div class="om-card gold">
              <div class="om-label">Priority Work Recommendation</div>
              <div class="om-big">Inspect Unit #2 <span class="om-badge warn">{unit2_priority}</span></div>
              <div class="om-sub" style="margin-top:10px;color:#e8f7ff">Bearing vibration is still below alarm limit, but the 7-day drift and thermal margin indicate an early mechanical degradation pattern. Recommended action is preventive inspection, not shutdown.</div>
              <div class="evidence">
                <div class="ev"><small>Vibration</small><b>{unit2_vib:.2f} mm/s • rising</b></div>
                <div class="ev"><small>Bearing Temp</small><b>{bearing_temp:.1f} °C • safe</b></div>
                <div class="ev"><small>Generation</small><b>{generation:.0f} MW • stable</b></div>
                <div class="ev"><small>Reservoir</small><b>{reservoir_pct:.1f}% • {hydro_window}</b></div>
                <div class="ev"><small>Grid</small><b>{freq:.2f} Hz • {grid_window}</b></div>
                <div class="ev"><small>AI Confidence</small><b>{confidence:.1f}%</b></div>
              </div>
            </div>
            <div class="om-card">
              <div class="om-label">Why Now?</div>
              <div class="om-sub" style="margin-top:9px;color:#e8f7ff">The maintenance window is favorable because reservoir storage and inflow are sufficient, grid export is stable, and Units #1/#3 can cover output during a short inspection window.</div>
              <div class="matrix2">
                <div class="mx2"><small>Operational Window</small><b>Next 24 hours</b></div>
                <div class="mx2"><small>Production Impact</small><b>Low / manageable</b></div>
                <div class="mx2"><small>Dam Safety Constraint</small><b>None</b></div>
                <div class="mx2"><small>Dispatch Strategy</small><b>Shift load to U1/U3</b></div>
              </div>
            </div>
          </div>
        </div>
        ''', unsafe_allow_html=True)

        left,right = st.columns([1.1,.9])
        with left:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Recommended Work Order", "from predictive analytics to field action")
            st.markdown(f'''
            <div class="workorder">
              <div class="wo"><small>Priority</small><b>{unit2_priority}</b></div>
              <div class="wo"><small>Department</small><b>Mechanical O&M</b></div>
              <div class="wo"><small>Equipment</small><b>Turbine Unit #2</b></div>
              <div class="wo"><small>Duration</small><b>{downtime_hours} hours</b></div>
              <div class="wo"><small>Required Skill</small><b>Vibration + alignment</b></div>
              <div class="wo"><small>Safety Permit</small><b>LOTO + confined access</b></div>
              <div class="wo"><small>Parts / Tools</small><b>Alignment tool, grease, sensor kit</b></div>
              <div class="wo"><small>Target Date</small><b>Tomorrow morning</b></div>
            </div>
            <div class="timeline2">
              <div class="tl2"><b>Now</b><span>Confirm vibration trend, compare Unit #2 with Unit #1/#3 baseline, and keep current dispatch.</span></div>
              <div class="tl2"><b>Next 24 hours</b><span>Open preventive inspection window for bearing alignment and coupling check while reservoir and grid conditions are favorable.</span></div>
              <div class="tl2"><b>Next 7 days</b><span>Perform dynamic balancing only if vibration remains above baseline after alignment inspection.</span></div>
              <div class="tl2"><b>Next 30 days</b><span>Schedule oil analysis and update bearing health baseline in the O&M model.</span></div>
            </div>
            ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="panel" style="margin-top:14px">', unsafe_allow_html=True)
            header("Cross-System Evidence", "recommendation is justified by more than one sensor")
            st.markdown(f'''
            <div class="ai-box"><div class="ai-title">AI Reasoning</div><div class="ai-text">Recommendation is not triggered by vibration alone. HOIP correlates Unit #2 vibration ({unit2_vib:.2f} mm/s), bearing temperature ({bearing_temp:.1f} °C), reservoir storage ({reservoir_pct:.1f}%), inflow ({inflow:.0f} m³/s), grid frequency ({freq:.2f} Hz), and dam safety indicators. Because hydrology and grid conditions are stable, this is a good moment for preventive O&M without sacrificing generation reliability.</div></div>
            <div class="action-strip">
              <div class="act"><small>Turbine</small><b>early drift</b></div>
              <div class="act"><small>Hydrology</small><b>window OK</b></div>
              <div class="act"><small>Dam</small><b>safe</b></div>
              <div class="act"><small>Grid</small><b>stable</b></div>
              <div class="act"><small>Decision</small><b>inspect</b></div>
            </div>
            ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with right:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Value Translation", "what happens if action is taken vs ignored")
            st.markdown(f'''
            <div class="om-card" style="margin-bottom:12px"><div class="om-label">If maintenance is done now</div><div class="om-big" style="font-size:30px">{downtime_hours} h <span class="om-badge">controlled</span></div><div class="om-sub">Short inspection window, manageable dispatch shift, low production impact.</div></div>
            <div class="om-card gold" style="margin-bottom:12px"><div class="om-label">If ignored</div><div class="om-big" style="font-size:30px">{if_ignored_hours} h <span class="om-badge warn">forced outage risk</span></div><div class="om-sub">Potential bearing damage, unplanned outage, and lost generation up to {lost_gwh:.1f} GWh.</div></div>
            <div class="valuebar"><span>Forced outage reduction</span><b>-62%</b></div><div class="barbg"><div class="barfill" style="width:62%"></div></div>
            <div class="valuebar"><span>Maintenance cost avoidance</span><b>-18%</b></div><div class="barbg"><div class="barfill" style="width:18%"></div></div>
            <div class="valuebar"><span>Generation availability uplift</span><b>+2.8%</b></div><div class="barbg"><div class="barfill" style="width:72%"></div></div>
            <div class="valuebar"><span>Estimated RUL extension</span><b>+7 months</b></div><div class="barbg"><div class="barfill" style="width:58%"></div></div>
            <div class="ai-box" style="margin-top:14px"><div class="ai-title">Executive O&M Note</div><div class="ai-text">Do not wait for alarm. The best value is created by intervening while the unit is still online, hydrology is supportive, and production can be shifted safely. This protects availability and avoids a larger forced-outage scenario.</div></div>
            ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f'''
        <div class="om-hero" style="margin-top:14px">
          <div class="om-label">Final O&M Decision Support</div>
          <div class="om-big" style="font-size:30px">Plan preventive inspection for Unit #2 tomorrow morning.</div>
          <div class="om-sub" style="color:#e8f7ff;margin-top:9px">Action owner: Mechanical O&M. Keep Unit #2 online today, shift load during inspection, and escalate only if vibration rises together with bearing temperature or generator load imbalance. Dam safety, hydrology, and grid conditions do not block the maintenance window.</div>
        </div>
        ''', unsafe_allow_html=True)

    elif page == "📊 ESG & Reporting":
        # Corporate-grade Reporting Center: converts all HOIP analytics into executive-ready reports.
        energy_today = data['energy_today']
        co2 = data['co2_avoided']
        plant_score = 96.8 + math.sin(t/28)*0.4
        safety_index = data['dam_health']
        gen_target = 102.3 + math.sin(t/31)*0.6
        water_security = 97.1 + math.sin(t/22)*0.5
        report_conf = 95.4 + math.sin(t/24)*0.4
        revenue_protected = 1.28 + math.sin(t/33)*0.04
        downtime_avoided = 16 + int(abs(math.sin(t/19))*3)
        saving_signal = 320 + int(abs(math.sin(t/18))*24)
        turb = live(22,3,17,.4)
        st.markdown("""
        <style>
        .report-hero{border:1px solid rgba(94,234,212,.22);background:linear-gradient(135deg,rgba(7,58,46,.80),rgba(4,19,30,.76));border-radius:26px;padding:22px;margin-bottom:16px;box-shadow:0 22px 60px rgba(0,0,0,.24);position:relative;overflow:hidden}.report-hero:before{content:"";position:absolute;right:-80px;top:-80px;width:260px;height:260px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.18),transparent 70%)}.report-eyebrow{font-size:12px;font-weight:900;letter-spacing:1.2px;color:#7fffd4;text-transform:uppercase}.report-title{font-size:32px;font-weight:950;letter-spacing:-1px;color:#f2fff9;margin-top:8px}.report-narrative{font-size:15px;line-height:1.65;color:#e8f7ff;margin-top:12px;max-width:960px}.report-decision{display:inline-flex;align-items:center;gap:8px;margin-top:14px;padding:10px 14px;border-radius:999px;border:1px solid rgba(103,232,165,.35);background:rgba(103,232,165,.10);font-size:12px;font-weight:900;color:#b8ffd6}.report-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-top:18px}.score-box{border:1px solid rgba(94,234,212,.16);background:rgba(255,255,255,.045);border-radius:18px;padding:13px}.score-box small{display:block;color:#a7cfc4;font-size:11px;font-weight:800}.score-box b{display:block;color:#fff;font-size:21px;font-weight:950;margin-top:5px}.report-card{border:1px solid rgba(94,234,212,.18);background:linear-gradient(160deg,rgba(8,54,45,.72),rgba(3,22,28,.66));border-radius:22px;padding:16px;margin-bottom:12px;position:relative;overflow:hidden}.report-card:before{content:"";position:absolute;right:-40px;top:-40px;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle,rgba(94,234,212,.13),transparent 70%)}.report-card h4{margin:0;color:#f2fff9;font-size:16px}.report-card p{margin:8px 0 0;color:#b6d8d0;font-size:12px;line-height:1.45}.report-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.report-btn{padding:7px 10px;border-radius:999px;border:1px solid rgba(94,234,212,.25);background:rgba(94,234,212,.08);color:#dffbf1;font-size:11px;font-weight:900}.report-btn.gold{border-color:rgba(255,209,102,.30);background:rgba(255,209,102,.09);color:#ffe8a3}.report-preview{border:1px solid rgba(94,234,212,.22);background:linear-gradient(180deg,rgba(244,255,250,.95),rgba(214,235,233,.92));border-radius:22px;padding:18px;color:#06151a;box-shadow:0 20px 52px rgba(0,0,0,.30)}.preview-top{display:flex;justify-content:space-between;border-bottom:2px solid rgba(6,21,26,.18);padding-bottom:12px;margin-bottom:12px}.preview-logo{font-weight:950;color:#0b4d3e;font-size:22px}.preview-title{font-weight:950;font-size:18px;color:#071923}.preview-section{border-left:4px solid #0ea5a6;padding-left:10px;margin:12px 0}.preview-section b{font-size:13px;color:#06151a}.preview-section p{font-size:11px;line-height:1.45;color:#223;margin:5px 0 0}.report-flow{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin-top:10px}.flow-step{border:1px solid rgba(94,234,212,.18);background:rgba(255,255,255,.045);border-radius:16px;padding:10px;text-align:center;font-size:11px;font-weight:900;color:#dffbf1;position:relative}.flow-step:not(:last-child):after{content:"→";position:absolute;right:-10px;top:50%;transform:translateY(-50%);color:#5eead4}.checklist{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}.check{font-size:12px;color:#dffbf1;background:rgba(255,255,255,.045);border:1px solid rgba(94,234,212,.12);border-radius:14px;padding:9px}.check:before{content:"✓";color:#67e8a5;font-weight:900;margin-right:7px}.dist-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}.dist{font-size:12px;color:#dffbf1;padding:9px;border-radius:14px;border:1px solid rgba(103,232,165,.18);background:rgba(103,232,165,.07)}.value-row{display:grid;grid-template-columns:1fr auto;gap:10px;padding:10px 0;border-bottom:1px solid rgba(94,234,212,.09)}.value-row:last-child{border-bottom:0}.value-row span{color:#c7d9e9;font-size:12px}.value-row b{color:#fff;font-size:13px}
        </style>
        """, unsafe_allow_html=True)

        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("Plant Score", f"{plant_score:.1f}", "/100", "Executive operation index")
        with c2: kpi("CO₂ Avoided", f"{co2:.0f}", "tCO₂e", "Estimated renewable impact")
        with c3: kpi("Report Confidence", f"{report_conf:.1f}", "%", "validated analytics coverage")
        with c4: kpi("Compliance", "GREEN", "", "no major deviation")

        st.markdown(f"""
        <div class="report-hero">
          <div class="report-eyebrow">Executive Report Center</div>
          <div class="report-title">Corporate-grade reporting from every HOIP intelligence layer.</div>
          <div class="report-narrative">During the last 24 hours, plant operation remains safe with positive water balance, reservoir storage inside the planned rule curve, normal dam safety indicators, stable turbine and electrical condition, and no environmental compliance deviation. Unit #2 bearing inspection is maintained as the main O&M note for the next maintenance window.</div>
          <div class="report-decision"><span class="pulse"></span> Overall recommendation: CONTINUE NORMAL OPERATION • generate daily executive report</div>
          <div class="report-grid">
            <div class="score-box"><small>Safety Index</small><b>{safety_index:.1f}%</b></div>
            <div class="score-box"><small>Generation Target</small><b>{gen_target:.1f}%</b></div>
            <div class="score-box"><small>Water Security</small><b>{water_security:.1f}%</b></div>
            <div class="score-box"><small>Maintenance Priority</small><b>LOW</b></div>
            <div class="score-box"><small>ESG Status</small><b>GREEN</b></div>
            <div class="score-box"><small>Forecast Horizon</small><b>72h</b></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        left, right = st.columns([1.08, .92])
        with left:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Corporate Report Library", "PDF • Word • Excel • PowerPoint")
            reports = [
                ("Shift Operation Report", "Operator-ready summary of generation, reservoir condition, active alarms, and handover notes.", "PDF", "Excel"),
                ("Daily Executive Report", "One-page board style report: plant score, water balance, safety, O&M priority, ESG status, and AI narrative.", "PDF", "PPT"),
                ("Reservoir Operation Report", "Rule curve, actual trajectory, inflow forecast, El Niño dry drift, hydrograph and spillway recommendation.", "PDF", "Excel"),
                ("Dam Safety Report", "Piezometer, seepage, deformation, trigger matrix, scenario forecast and decision recommendation.", "PDF", "Word"),
                ("Predictive O&M Report", "Recommended work orders, evidence, maintenance window, if-done vs if-ignored value translation.", "PDF", "Excel"),
                ("Monthly ESG & Compliance Report", "Renewable energy, CO₂ avoided, water quality, air quality, sediment watch, and compliance narrative.", "PDF", "Word"),
            ]
            for title, desc, a, b in reports:
                st.markdown(f'<div class="report-card"><h4>{title}</h4><p>{desc}</p><div class="report-actions"><span class="report-btn">Generate {a}</span><span class="report-btn gold">Generate {b}</span><span class="report-btn">Schedule</span></div></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="panel" style="margin-top:14px">', unsafe_allow_html=True)
            header("Report Generation Workflow", "sensor to signed corporate output")
            st.markdown('<div class="report-flow"><div class="flow-step">Sensor</div><div class="flow-step">Validation</div><div class="flow-step">Analytics</div><div class="flow-step">Correlation</div><div class="flow-step">AI Recommendation</div><div class="flow-step">Report</div><div class="flow-step">Archive</div></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with right:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Live Report Preview", "Daily Executive Report")
            st.markdown(f"""
            <div class="report-preview">
              <div class="preview-top"><div><div class="preview-logo">KHN</div><div style="font-size:10px;color:#345">PT Kayan Hydropower Nusantara</div></div><div style="text-align:right"><div class="preview-title">HOIP Daily Executive Report</div><div style="font-size:10px;color:#456">08 Jul 2026 • Auto-generated</div></div></div>
              <div class="preview-section"><b>Executive Summary</b><p>Plant operation remains stable. Reservoir storage is inside operating rule curve. No dam safety anomaly detected. Unit #2 requires preventive bearing inspection in the next maintenance window.</p></div>
              <div class="preview-section"><b>Key KPI</b><p>Plant score {plant_score:.1f}/100 • Energy {energy_today:.2f} GWh • CO₂ avoided {co2:.0f} tCO₂e • Compliance GREEN.</p></div>
              <div class="preview-section"><b>AI Recommendation</b><p>Continue normal dispatch. Maintain spillway closed. Keep dam safety watch frequency normal unless rainfall persists above 10 mm/h for 48 hours.</p></div>
              <div class="preview-section"><b>O&M Note</b><p>Plan Unit #2 inspection tomorrow morning. Hydrology and grid condition support short controlled maintenance window.</p></div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="panel" style="margin-top:14px">', unsafe_allow_html=True)
            header("Auto Included Sections", "from pages already built")
            sections = ["Weather & hydrology forecast", "Reservoir rule curve", "Dam safety decision matrix", "Water quality & sedimentation", "Air quality & community ESG", "Turbine & electrical health", "Correlation impact chain", "AI recommendation center", "Predictive O&M value", "Appendix & audit trail"]
            st.markdown('<div class="checklist">' + ''.join([f'<div class="check">{s}</div>' for s in sections]) + '</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        a,b,c = st.columns([.9,.8,.9])
        with a:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Distribution Center", "email • WhatsApp • API")
            dist = ["Plant Manager", "Operation Manager", "Dam Safety Engineer", "Maintenance Lead", "Environmental Officer", "CEO / Board", "Regulator", "Project Archive"]
            st.markdown('<div class="dist-grid">' + ''.join([f'<div class="dist">● {d}</div>' for d in dist]) + '</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with b:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Report Quality", "data governance")
            metric("Sensor Coverage", "96.8%")
            metric("Validated Sensors", "94.2%")
            metric("Manual / Lab Validation", "2 parameters")
            metric("Turbidity Note", f"{turb:.1f} NTU • sediment watch")
            metric("AI Confidence", f"{report_conf:.1f}%")
            st.markdown('</div>', unsafe_allow_html=True)
        with c:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Business Value Summary", "rupiah narrative")
            st.markdown(f"""
            <div class="value-row"><span>Revenue Protected</span><b>Rp {revenue_protected:.2f} B</b></div>
            <div class="value-row"><span>Downtime Avoided</span><b>{downtime_avoided} hours</b></div>
            <div class="value-row"><span>Maintenance Saving Signal</span><b>Rp {saving_signal} M</b></div>
            <div class="value-row"><span>Generation Loss Avoided</span><b>18 MWh</b></div>
            <div class="value-row"><span>CO₂ Avoided</span><b>{co2:.0f} tCO₂e</b></div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="ai-box" style="margin-top:14px">
          <div class="ai-title">Corporate Report Narrative</div>
          <div class="ai-text">All analytics from Weather, Reservoir & Hydrology, Water Quality, Air Quality, Dam Intelligence, Powerhouse & Turbine, Electrical & Switchyard, Correlation Engine, AI Recommendation, and Predictive O&M are consolidated into one executive-ready reporting package. The output is suitable for shift handover, management review, monthly ESG reporting, and regulator-facing documentation.</div>
        </div>
        """, unsafe_allow_html=True)


    elif page == "🚀 Implementation Roadmap":
        digital = 86 + (math.sin(t/33)*1.2)
        ai_ready = 4
        enterprise = 95 + (math.sin(t/39)*0.7)
        subsystems = 12
        c1,c2,c3,c4 = st.columns(4)
        with c1: kpi("Digitalization", f"{digital:.0f}", "%", "Telemetry to intelligence maturity")
        with c2: kpi("Subsystem Integrated", f"{subsystems}/12", "", "Weather, water, dam, turbine, grid, ESG")
        with c3: kpi("AI Readiness", f"Level {ai_ready}", "", "Recommendation + decision support")
        with c4: kpi("Enterprise Readiness", f"{enterprise:.0f}", "%", "Operation center rollout grade")

        st.markdown('''
        <style>
        .roadmap-hero{border:1px solid rgba(94,234,212,.22);background:linear-gradient(145deg,rgba(7,55,46,.78),rgba(4,20,30,.72));border-radius:26px;padding:18px;position:relative;overflow:hidden;box-shadow:0 22px 60px rgba(0,0,0,.22)}
        .roadmap-hero:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 18% 8%,rgba(94,234,212,.16),transparent 28%),radial-gradient(circle at 92% 0%,rgba(255,209,102,.10),transparent 25%);pointer-events:none}
        .roadmap-title{font-size:24px;font-weight:950;letter-spacing:-.5px;color:#f2fff9;position:relative;z-index:1}.roadmap-sub{font-size:13px;color:#a7cfc4;margin-top:6px;position:relative;z-index:1}
        .phase-card{border:1px solid rgba(94,234,212,.18);background:linear-gradient(135deg,rgba(9,57,48,.72),rgba(5,24,33,.68));border-radius:22px;padding:16px;margin:12px 0;position:relative;overflow:hidden}
        .phase-card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:linear-gradient(180deg,#5eead4,#67e8a5,#ffd166)}
        .phase-meta{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:10px}.phase-no{font-size:11px;font-weight:900;color:#7fffd4;letter-spacing:.9px;text-transform:uppercase}.phase-status{font-size:10px;font-weight:900;border:1px solid rgba(103,232,165,.35);background:rgba(103,232,165,.10);color:#b8ffd6;border-radius:999px;padding:5px 8px}.phase-name{font-size:18px;font-weight:950;color:#eef8ff;letter-spacing:-.25px}.phase-text{font-size:12px;color:#a9bfd3;line-height:1.55;margin:7px 0 10px}.deliver-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.deliver{font-size:11px;color:#d7fff3;background:rgba(255,255,255,.045);border:1px solid rgba(94,234,212,.12);border-radius:999px;padding:6px 8px}.road-progress{height:7px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden;margin-top:12px}.road-progress span{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,#5eead4,#67e8a5,#ffd166);box-shadow:0 0 18px rgba(94,234,212,.28)}
        .cap-card{border:1px solid rgba(94,234,212,.18);background:linear-gradient(145deg,rgba(7,44,43,.72),rgba(4,17,28,.70));border-radius:22px;padding:16px;margin-bottom:12px}.cap-title{font-size:14px;font-weight:900;color:#7fffd4;text-transform:uppercase;letter-spacing:.8px;margin-bottom:10px}.cap-row{display:grid;grid-template-columns:150px 1fr 45px;gap:10px;align-items:center;padding:7px 0;border-bottom:1px solid rgba(94,234,212,.08)}.cap-row:last-child{border-bottom:0}.cap-name{font-size:12px;color:#c7d9e9}.cap-bar{height:8px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden}.cap-bar span{display:block;height:100%;background:linear-gradient(90deg,#5eead4,#67e8a5);border-radius:99px}.cap-val{font-size:12px;font-weight:900;color:#fff;text-align:right}
        .value-card{display:grid;grid-template-columns:125px 1fr;gap:12px;border-bottom:1px solid rgba(94,234,212,.10);padding:11px 0}.value-card:last-child{border-bottom:0}.value-role{font-size:12px;font-weight:900;color:#eef8ff}.value-desc{font-size:12px;color:#a9bfd3;line-height:1.45}.timeline-strip{display:grid;grid-template-columns:repeat(8,1fr);gap:8px;margin-top:14px}.timeline-pill{border:1px solid rgba(94,234,212,.16);background:rgba(255,255,255,.045);border-radius:16px;padding:10px;text-align:center;min-height:76px}.timeline-pill b{font-size:11px;color:#eef8ff}.timeline-pill small{display:block;color:#a7cfc4;font-size:10px;margin-top:5px}
        </style>
        ''', unsafe_allow_html=True)

        st.markdown('''
        <div class="roadmap-hero">
          <div class="roadmap-title">Implementation Roadmap</div>
          <div class="roadmap-sub">From field telemetry to operational intelligence, AI decision support, predictive asset management, and executive-grade reporting.</div>
        </div>
        ''', unsafe_allow_html=True)

        left,right = st.columns([1.15,.85])
        with left:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Enterprise Implementation Journey", "Structured rollout based on the HOIP subsystems already demonstrated")
            phases = [
                ("Phase 1", "Digital Foundation", "Connect plant data into one trusted operational layer: field telemetry, gateway communication, historian, and dashboard foundation.", ["Weather", "Air Quality", "Water Quality", "Reservoir", "Dam Sensors", "Turbine", "Electrical", "MQTT", "Modbus"], 100),
                ("Phase 2", "Operational Intelligence", "Turn monitoring into operational situation awareness across hydrology, reservoir operation, civil safety, generation, and grid delivery.", ["Digital Twin", "Live KPI", "Subsystem Pages", "Operator View", "Root Cause", "Situation Awareness"], 100),
                ("Phase 3", "Correlation & Impact Engine", "Make every subsystem explain its effect on the others: rainfall to inflow, reservoir to dam safety, turbine to dispatch, water quality to ESG.", ["Risk Chains", "Cause-Effect", "Hydrograph", "Sediment Watch", "Blind Spot Reduction", "Impact Matrix"], 100),
                ("Phase 4", "AI Decision Intelligence", "Convert analytics into recommendations with evidence, confidence, decision owner, operational trigger, and expected benefit.", ["AI Brief", "Dispatch Advice", "Dam Watch", "O&M Priority", "ESG Advisor", "Operator Approval"], 95),
                ("Phase 5", "Predictive Asset Management", "Translate vibration, bearing temperature, seepage, pressure, transformer loading, and breaker health into maintenance action and financial risk.", ["Work Order", "RUL", "Maintenance Window", "Cost Avoidance", "Unit Priority", "Failure Prevention"], 90),
                ("Phase 6", "Executive & ESG Intelligence", "Generate corporate-grade reports for management, O&M, dam safety, ESG, regulator review, audit trail, and automated distribution.", ["PDF Report", "Executive KPI", "ESG", "Audit Trail", "Email/WA", "Board Pack"], 92),
            ]
            for no,name,desc,items,pct in phases:
                chips=''.join([f'<div class="deliver">✓ {x}</div>' for x in items])
                st.markdown(f'''
                <div class="phase-card">
                  <div class="phase-meta"><div class="phase-no">{no}</div><div class="phase-status">{pct}% READY</div></div>
                  <div class="phase-name">{name}</div>
                  <div class="phase-text">{desc}</div>
                  <div class="deliver-grid">{chips}</div>
                  <div class="road-progress"><span style="width:{pct}%"></span></div>
                </div>
                ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with right:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            header("Platform Capability Matrix", "Maturity view for enterprise rollout")
            caps=[("Telemetry",100),("Monitoring",100),("Analytics",100),("Correlation",100),("AI Recommendation",95),("Predictive Maintenance",90),("Corporate Reporting",92),("Digital Twin",84),("Optimization Engine",68),("Autonomous Operation",32)]
            rows=''.join([f'<div class="cap-row"><div class="cap-name">{n}</div><div class="cap-bar"><span style="width:{v}%"></span></div><div class="cap-val">{v}%</div></div>' for n,v in caps])
            st.markdown(f'<div class="cap-card"><div class="cap-title">Readiness by Capability</div>{rows}</div>', unsafe_allow_html=True)

            st.markdown('<div class="cap-card"><div class="cap-title">Business Value Delivered</div>', unsafe_allow_html=True)
            values=[("Board", "One operational truth across water, dam, generation, asset health, ESG, and business value."), ("Operator", "Faster daily decisions: spillway, dispatch, monitoring interval, and abnormal condition response."), ("Engineer", "Root-cause visibility from hydrology, instrumentation, turbine, electrical, and environmental evidence."), ("Maintenance", "Risk-based work orders, inspection priority, maintenance window selection, and downtime avoidance."), ("ESG", "Renewable impact, water quality, air quality, sediment watch, compliance narrative, and corporate reporting."), ("Future", "Foundation for optimization engine, semi-autonomous dispatch, and autonomous dam operation governance.")]
            for role,desc in values:
                st.markdown(f'<div class="value-card"><div class="value-role">{role}</div><div class="value-desc">{desc}</div></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            timeline=[("Telemetry","Field data"),("Validation","Trusted data"),("Analytics","Subsystem insight"),("Correlation","Cause-effect"),("AI","Recommendation"),("O&M","Action"),("Report","Corporate output"),("Autonomy","Future")]
            html=''.join([f'<div class="timeline-pill"><b>{a}</b><small>{b}</small></div>' for a,b in timeline])
            st.markdown(f'<div class="cap-card"><div class="cap-title">Roadmap Logic</div><div class="timeline-strip">{html}</div></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('''
        <div class="ai-box" style="margin-top:14px">
          <div class="ai-title">Closing Executive Message</div>
          <div class="ai-text">HOIP is implemented as a staged enterprise platform: first connecting every subsystem, then correlating hydrology, dam safety, generation, asset health, environmental quality, and ESG into one decision layer. The roadmap shows how PT Kayan can move from monitoring to AI-assisted operation, predictive maintenance, corporate reporting, and eventually governed semi-autonomous hydropower operation.</div>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('<div class="footer-note">HOIP v1.0 Premium POC • Hydropower Operational Intelligence Platform • Wavetek Industrial Intelligence Concept</div>', unsafe_allow_html=True)



# Render app body. Subsystem Command Center uses local JS animation, no full app reload.
_render_live_body()
