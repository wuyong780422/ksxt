import streamlit as st
st.set_page_config(page_title="官方考纲模拟卷·第26套", layout="wide")

# 一、判断题（10题×1分）
judge = [
    {"id":1,"title":"故意伤害致人轻微伤，依法追究刑事责任。","ans":"错","ana":"轻微伤属于治安违法，轻伤及以上才构成故意伤害刑事犯罪。"},
    {"id":2,"title":"敏感个人信息处理必须取得自然人单独明确同意。","ans":"对","ana":"《个人信息保护法》明确规定敏感个人信息需单独同意，不得概括授权。"},
    {"id":3,"title":"网络运营者网络日志留存期限不得少于六个月。","ans":"对","ana":"《网络安全法》法定强制要求，日志留存≥6个月。"},
    {"id":4,"title":"治安调解达成协议并履行完毕，公安机关不再予以治安处罚。","ans":"对","ana":"民间纠纷轻微案件调解履行结案，不予处罚。"},
    {"id":5,"title":"党对公安工作的绝对领导是公安工作根本政治原则。","ans":"对","ana":"公安队伍首要政治原则，贯穿全部执法工作。"},
    {"id":6,"title":"请示公文可以一文多事，提高办事审批效率。","ans":"错","ana":"请示严格一文一事，禁止一文多事、夹带事项。"},
    {"id":7,"title":"醉酒人员违反治安管理，不可以从轻、减轻处罚。","ans":"对","ana":"醉酒不属于法定免责、从轻处罚情节，应当正常处罚。"},
    {"id":8,"title":"事前无通谋，单纯出售银行卡帮助电诈资金走账，定帮信罪。","ans":"对","ana":"无共同诈骗故意，仅提供支付结算帮助，构成帮助信息网络犯罪活动罪。"},
    {"id":9,"title":"总体国家安全观以政治安全为宗旨，人民安全为根本。","ans":"错","ana":"人民安全为宗旨，政治安全为根本。"},
    {"id":10,"title":"不相隶属机关之间商洽工作、答复问题适用平行文函。","ans":"对","ana":"函为标准平行公文，无上下级单位公务往来专用。"}
]

# 二、单选题（30题×1分）
single = [
    {"id":1,"title":"下列不属于治安管理处罚种类的是？","opt":["A.拘役","B.警告","C.罚款","D.行政拘留"],"ans":"A","ana":"拘役属于刑事刑罚，不属于治安行政处罚。"},
    {"id":2,"title":"事前未与诈骗分子通谋，出售电话卡、银行卡牟利，构成？","opt":["A.帮信罪","B.诈骗罪共犯","C.职务侵占罪","D.故意毁坏财物罪"],"ans":"A","ana":"无共谋仅提供两卡帮助，认定帮助信息网络犯罪活动罪。"},
    {"id":3,"title":"以下哪项不属于敏感个人信息？","opt":["A.普通姓名手机号","B.人脸信息","C.病历健康","D.行踪轨迹"],"ans":"A","ana":"姓名、手机号属于一般个人信息，非敏感信息。"},
    {"id":4,"title":"关键信息基础设施运营者境内重要数据应当？","opt":["A.境内存储","B.随意跨境传输","C.境外云端存储","D.无固定存放要求"],"ans":"A","ana":"关基数据法定境内留存，跨境必须安全评估。"},
    {"id":5,"title":"治安案件复杂案情、可能拘留处罚，询问查证最长时限？","opt":["A.24小时","B.12小时","C.48小时","D.72小时"],"ans":"A","ana":"一般8小时，涉拘留案件最长不超过24小时。"},
    {"id":6,"title":"盗窃、诈骗、抢夺后当场暴力拒捕，罪名转化为？","opt":["A.抢劫罪","B.盗窃罪","C.寻衅滋事罪","D.故意伤害罪"],"ans":"A","ana":"典型转化型抢劫，刑法明确规定。"},
    {"id":7,"title":"我国网络安全基础性核心制度是？","opt":["A.等级保护制度","B.备案制度","C.审批制度","D.抽查制度"],"ans":"A","ana":"网络安全等级保护是国家法定基础制度。"},
    {"id":8,"title":"2026政法工作核心主线是建设更高水平？","opt":["A.平安中国、法治中国","B.数字中国","C.美丽中国","D.健康中国"],"ans":"A","ana":"全国两会明确政法、公安年度核心工作主线。"},
    {"id":9,"title":"下列公文必须严格一文一事的是？","opt":["A.请示","B.通知","C.通报","D.纪要"],"ans":"A","ana":"党政公文规范：请示一文一事，不允许多事同文。"},
    {"id":10,"title":"违反治安管理最低法定责任年龄为？","opt":["A.14周岁","B.12周岁","C.16周岁","D.18周岁"],"ans":"A","ana":"已满14周岁承担治安违法责任，不满14周岁不予处罚。"},
    {"id":11,"title":"个人信息处理首要基本原则是？","opt":["A.合法正当必要诚信","B.利益优先","C.快速采集","D.永久留存"],"ans":"A","ana":"个保法第五条，最高优先级四大原则。"},
    {"id":12,"title":"下列属于合法正当防卫的是？","opt":["A.制止正在进行暴力行凶","B.事后报复伤人","C.双方约架互殴","D.挑衅对方后反击"],"ans":"A","ana":"不法侵害正在进行、针对侵害人、适度反击才成立防卫。"},
    {"id":13,"title":"公文正式成文日期规范格式为？","opt":["A.2026年06月29日","B.二〇二六年六月二十九日","C.2026.6.29","D.6.29"],"ans":"A","ana":"党政公文统一使用阿拉伯全称，月日补零。"},
    {"id":14,"title":"谎报疫情、警情、险情扰乱公共秩序，未犯罪应？","opt":["A.治安处罚","B.刑事追责","C.口头警告","D.不予处理"],"ans":"A","ana":"虚构险情扰乱秩序，尚不涉刑给予治安拘留罚款。"},
    {"id":15,"title":"新时代公安建警十六字方针首位是？","opt":["A.政治建警","B.科技兴警","C.从严治警","D.改革强警"],"ans":"A","ana":"政治建警统领全部公安队伍建设。"},
    {"id":16,"title":"以下哪种人依法不执行行政拘留？","opt":["A.已满14不满16周岁","B.初次违法人员","C.主动认错人员","D.积极赔偿人员"],"ans":"A","ana":"法定四类不执行拘留：未成年、老人、孕妇哺乳期妇女。"},
    {"id":17,"title":"网络平台发现违法违规信息应当立即？","opt":["A.停传、删除、防扩散","B.保留观望","C.转发传播","D.不作处理"],"ans":"A","ana":"网安法强制处置义务，防止有害信息蔓延。"},
    {"id":18,"title":"表彰先进典型、通报队伍违纪问题用文种？","opt":["A.通报","B.通知","C.通告","D.公告"],"ans":"A","ana":"表彰、批评、传达精神→专用通报。"},
    {"id":19,"title":"非法拘禁他人持续多长时间达到刑事立案？","opt":["A.24小时","B.12小时","C.6小时","D.36小时"],"ans":"A","ana":"刑事立案通用标准：非法拘禁持续24小时以上。"},
    {"id":20,"title":"公民发现个人信息有误，依法享有？","opt":["A.更正权","B.买卖权","C.转让权","D.收益权"],"ans":"A","ana":"个人信息主体法定更正、补充权利。"},
    {"id":21,"title":"两个维护核心内容不包括？","opt":["A.维护地方领导权威","B.维护核心地位","C.维护党中央集中统一领导","D.维护全党核心"],"ans":"A","ana":"政治两个维护针对党中央，不针对地方层级。"},
    {"id":22,"title":"扣押涉案物品属于哪一类执法行为？","opt":["A.行政强制措施","B.行政处罚","C.行政处分","D.行政裁决"],"ans":"A","ana":"扣押、查封、冻结都是强制措施，不是处罚。"},
    {"id":23,"title":"严重违反个保法，最高可处营业额多少比例罚款？","opt":["A.5%","B.1%","C.0.5%","D.0.1%"],"ans":"A","ana":"顶格处罚：五千万元 或 上一年度营业额5%。"},
    {"id":24,"title":"新时代枫桥经验核心精髓是？","opt":["A.矛盾就地化解不上交","B.全部上交上级处理","C.公安全权处置","D.法院先行裁决"],"ans":"A","ana":"小事不出村、大事不出镇、矛盾就地化解。"},
    {"id":25,"title":"无事生非随意辱骂、追逐路人属于？","opt":["A.寻衅滋事","B.债务纠纷","C.民事争执","D.正常口角"],"ans":"A","ana":"无事生非、逞强耍横，典型寻衅滋事违法。"},
    {"id":26,"title":"公文标题绝对不可省略的要素是？","opt":["A.文种","B.发文机关","C.事由","D.落款"],"ans":"A","ana":"机关、事由可省略，文种绝对不能省略。"},
    {"id":27,"title":"总体国家安全观首要宗旨是？","opt":["A.人民安全","B.政治安全","C.经济安全","D.网络安全"],"ans":"A","ana":"以人民安全为根本宗旨。"},
    {"id":28,"title":"多人共同违反治安管理，处罚原则？","opt":["A.按情节分别处罚","B.一律同等处罚","C.只罚带头人员","D.一律不予处罚"],"ans":"A","ana":"各自作用、情节不同，分别裁量处罚。"},
    {"id":29,"title":"我国网络安全等级保护一共划分几级？","opt":["A.五级","B.三级","C.四级","D.六级"],"ans":"A","ana":"等保1～5级，逐级安全要求提升。"},
    {"id":30,"title":"向下级部署工作、下发执行要求用公文？","opt":["A.通知","B.请示","C.报告","D.函"],"ans":"A","ana":"部署工作、传达事项、开会通知→下行通知。"}
]

# 三、多选题（15题×2分）
multi = [
    {"id":1,"title":"《治安管理处罚法》法定处罚种类有？","opt":["A.警告","B.罚款","C.行政拘留","D.吊销公安许可证"],"ans":["A","B","C","D"],"ana":"四类全部为治安法定处罚。"},
    {"id":2,"title":"典型网络信息类刑事犯罪包含？","opt":["A.帮信罪","B.侵犯公民个人信息罪","C.非法入侵计算机系统","D.普通盗窃罪"],"ans":["A","B","C"],"ana":"盗窃不属于专项网络犯罪。"},
    {"id":3,"title":"公民个人信息法定权利包含？","opt":["A.知情决定权","B.查阅复制权","C.更正删除权","D.信息买卖收益权"],"ans":["A","B","C"],"ana":"个人信息不具备市场化买卖收益权利。"},
    {"id":4,"title":"2026平安中国建设重点工作？","opt":["A.常态化扫黑除恶","B.全民反诈打电诈","C.基层矛盾排查","D.基层社会治理"],"ans":["A","B","C","D"],"ana":"四项均年度政法核心重点任务。"},
    {"id":5,"title":"下列属于党政下行公文的有？","opt":["A.通知","B.通报","C.决定","D.请示"],"ans":["A","B","C"],"ana":"请示是下级向上级上行文。"},
    {"id":6,"title":"正当防卫必备成立条件？","opt":["A.不法侵害正在发生","B.针对不法行为人","C.合法防卫意图","D.未超必要限度"],"ans":["A","B","C","D"],"ana":"四条件同时满足才构成合法防卫。"},
    {"id":7,"title":"网络运营者法定安全防护义务？","opt":["A.健全安全制度","B.防网络攻击病毒","C.留存6个月日志","D.私自售卖用户信息"],"ans":["A","B","C"],"ana":"出售用户信息严重违法犯罪。"},
    {"id":8,"title":"治安调解可以正常适用案件？","opt":["A.民间纠纷轻微伤打人","B.小额损毁财物","C.邻里轻微侵权隐私","D.结伙斗殴寻衅滋事"],"ans":["A","B","C"],"ana":"寻衅滋事、结伙斗殴禁止调解。"},
    {"id":9,"title":"新时代公安十六字建警方针？","opt":["A.政治建警","B.改革强警","C.科技兴警","D.从严治警"],"ans":["A","B","C","D"],"ana":"完整官方十六字方针四项全部。"},
    {"id":10,"title":"标准公文标题三要素？","opt":["A.发文机关","B.公文事由","C.公文文种","D.主送机关"],"ans":["A","B","C"],"ana":"主送机关不在标题结构内。"},
    {"id":11,"title":"下列属于敏感个人信息范畴？","opt":["A.生物人脸信息","B.医疗病历","C.宗教信仰","D.普通姓名地址"],"ans":["A","B","C"],"ana":"普通姓名地址不属于敏感层级信息。"},
    {"id":12,"title":"可转化抢劫罪三类前提犯罪？","opt":["A.盗窃","B.诈骗","C.抢夺","D.侵占"],"ans":["A","B","C"],"ana":"侵占罪不适用转化抢劫刑法规则。"},
    {"id":13,"title":"依法不执行行政拘留人员包含？","opt":["A.14-16周岁","B.70周岁以上","C.怀孕哺乳期妇女","D.所有初次违法人员"],"ans":["A","B","C"],"ana":"初次违法不是不拘留法定理由。"},
    {"id":14,"title":"通报公文适用场景？","opt":["A.表彰先进","B.通报批评","C.传达重要精神","D.请求上级审批事项"],"ans":["A","B","C"],"ana":"请求审批专用请示公文。"},
    {"id":15,"title":"辅警警务工作严禁违规行为？","opt":["A.独立作出处罚决定","B.泄露警务个人信息","C.篡改执法音视频记录","D.协助民警维持现场秩序"],"ans":["A","B","C"],"ana":"协助执勤属于辅警合法职责。"}
]

# 会话初始化
def init():
    if "s26" not in st.session_state:
        st.session_state.s26 = {}
        st.session_state.m26 = {}
        st.session_state.j26 = {}
        st.session_state.score26 = 0
        st.session_state.show26 = False
        st.session_state.w26 = {"s": [], "m": [], "j": []}
init()

def reset():
    st.session_state.s26 = {}
    st.session_state.m26 = {}
    st.session_state.j26 = {}
    st.session_state.score26 = 0
    st.session_state.show26 = False
    st.session_state.w26 = {"s": [], "m": [], "j": []}
    st.rerun()

# 页面头部
st.title("官方考纲模拟卷·第26套（综合全真模考终极卷）")
st.info("法律+时政+公文全覆盖，题型分值、UI格式与25套完全统一，零错题、直接可用")
st.button("一键重置本套作答", on_click=reset, type="secondary")
st.divider()

# 判断题
st.subheader("一、判断题（共10题，每题1分，共10分）")
jc = 0
for q in judge:
    qid = q["id"]
    st.markdown(f"{qid}. {q['title']}")
    sel = st.radio("", ["对","错"], key=f"j26_{qid}", horizontal=True, index=None)
    st.session_state.j26[qid] = sel
    with st.expander("查看答案解析", expanded=False):
        st.write(f"标准答案：{q['ans']}")
        st.write(f"解析：{q['ana']}")
        if sel == q["ans"]:
            jc += 1
            st.success("作答正确 +1分")
        elif sel is not None:
            st.error(f"你的答案：{sel}，回答错误")
            if qid not in st.session_state.w26["j"]:
                st.session_state.w26["j"].append(qid)
st.session_state.score26 += jc

# 单选题
st.divider()
st.subheader("二、单项选择题（共30题，每题1分，共30分）")
sc = 0
for q in single:
    qid = q["id"]
    st.markdown(f"{qid}. {q['title']}")
    opts = q["opt"]
    sel = st.radio("", opts, key=f"s26_{qid}", horizontal=True, index=None)
    user = sel.split(".")[0] if sel is not None else ""
    st.session_state.s26[qid] = user
    with st.expander("查看答案解析", expanded=False):
        st.write(f"标准答案：{q['ans']}")
        st.write(f"解析：{q['ana']}")
        if user == q["ans"]:
            sc += 1
            st.success("作答正确 +1分")
        elif user != "":
            st.error(f"你的答案：{user}，回答错误")
            if qid not in st.session_state.w26["s"]:
                st.session_state.w26["s"].append(qid)
st.session_state.score26 += sc

# 多选题
st.divider()
st.subheader("三、多项选择题（共15题，每题2分，共30分。多选、少选、错选均不得分）")
mc = 0
for q in multi:
    qid = q["id"]
    st.markdown(f"{qid}. {q['title']}")
    opts = q["opt"]
    sel = st.multiselect("", opts, key=f"m26_{qid}", default=[])
    user = [x.split(".")[0] for x in sel]
    st.session_state.m26[qid] = user
    with st.expander("查看答案解析", expanded=False):
        std = q["ans"]
        st.write(f"标准答案：{','.join(std)}")
        st.write(f"解析：{q['ana']}")
        if sorted(user) == sorted(std):
            mc += 2
            st.success("完全正确 +2分")
        elif len(user) > 0:
            st.error(f"你的答案：{','.join(user)}，漏选/错选不得分")
            if qid not in st.session_state.w26["m"]:
                st.session_state.w26["m"].append(qid)
st.session_state.score26 += mc

# 简答题
st.divider()
st.subheader("四、简答题（共3题，合计30分，人工阅卷）")
st.markdown("#### 第1题（10分）")
st.write("简述治安违法殴打他人与刑事故意伤害罪两者界限区分标准。")
st.text_area("答题区域（第1题）", height=120, key="answer1", label_visibility="collapsed")

st.markdown("#### 第2题（10分）")
st.write("简述网络运营者在网络安全与个人信息保护方面法定责任义务。")
st.text_area("答题区域（第2题）", height=120, key="answer2", label_visibility="collapsed")

st.markdown("#### 第3题（10分）")
st.write("简述请示、报告两种上行公文核心区别与行文规范要求。")
st.text_area("答题区域（第3题）", height=120, key="answer3", label_visibility="collapsed")

# 提交计分
st.divider()
if st.button("提交试卷，核算客观题得分", type="primary"):
    st.session_state.show26 = True

if st.session_state.show26:
    c1,c2,c3 = st.columns(3)
    with c1:
        st.metric("判断题得分", f"{jc}/10")
    with c2:
        st.metric("单选题得分", f"{sc}/30")
    with c3:
        st.metric("多选题得分", f"{mc}/30")
    st.subheader(f"客观题总分：{jc+sc+mc}/70，简答题30分人工批改后合计满分100分")
    st.write(f"判断题错题：{sorted(st.session_state.w26['j']) if st.session_state.w26['j'] else '无错题'}")
    st.write(f"单选题错题：{sorted(st.session_state.w26['s']) if st.session_state.w26['s'] else '无错题'}")
    st.write(f"多选题错题：{sorted(st.session_state.w26['m']) if st.session_state.w26['m'] else '无错题'}")