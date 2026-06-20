import streamlit as st
# 运行命令streamlit run Home.py
st.set_page_config(page_title="模拟考试系统", layout="wide")

st.markdown("# 📝 模拟系统")
st.divider()
st.subheader("官方考情｜全新试卷｜匹配招聘")
st.info("题型结构：单选+多选+判断客观题80分 + 公文改错/写作主观题20分")
st.divider()

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.subheader("📘 测试一")
    st.markdown("综合全真卷\n法律+时政+公文")
    st.info("入门摸底测试")

with c2:
    st.subheader("📗 测试二")
    st.markdown("法律专项卷\n纯公安法律重难点")
    st.info("主攻高分模块")

with c3:
    st.subheader("📙 测试三")
    st.markdown("时政公文专项卷\n攻克主观题弱项")
    st.info("提分专项训练")

with c4:
    st.subheader("📕 测试四")
    st.markdown("【官方方案】真题卷A\n标准100分配比")
    st.success("全真考场模式")

with c5:
    st.subheader("📓 测试五")
    st.markdown("【官方方案】真题卷B\n全新独立题库")
    st.success("考前冲刺模考")

st.divider()
st.warning("💡 使用方法：左侧侧边栏点击对应试卷即可切换｜5套题库**100%无重复**｜完全对标2026辅警招聘笔试大纲")
