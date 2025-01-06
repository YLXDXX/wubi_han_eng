--下在的两个函数 null_add_translator 和 null_add_filter
--是在候选项为空的时候，进行输入的英文补全和英文分词


--当候选项为空的时候，作补充
--需在 translator 中加入 - "lua_translator@null_add_translator"
local function if_null_add_translator(input, seg)
    --获取键盘上输入的字符串
    --local inputKeys = env.engine.context.input
    yield(Candidate("null_add", seg.start, seg._end, input, "   ⌨︎"))
end

return if_null_add_translator
