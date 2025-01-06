--下在的两个函数 null_add_translator 和 null_add_filter
--是在候选项为空的时候，进行输入的英文补全和英文分词

--执行系统命令，分词使用
local function cmd_capture(cmd)
   local f = assert(io.popen(cmd, 'r'))
   local s = assert(f:read('*a'))
   f:close()
   return s
end

--当候选项为空的时候，作补充
--需在 filter 中加入 - lua_filter@null_add_filter
local function if_null_add_filter(input, seg, env)
    local null = {}
    local num=0
    for cand in input:iter() do
       num=num+1
       if (cand.type == "null_add") then
          table.insert(null, cand)
       else
           if (cand.comment ~= "   ⌨︎ 〕") then
               --此判断，是为去除拼音反查时的输入字符显示
               yield(cand)
           end
       end
    end
    for i, cand in ipairs(null) do
        if (num == 1) then
            yield(cand)
            local auto=cmd_capture("~/.local/share/fcitx5/rime/lua/easy_en/fengci/wordninja" .. " -n '" .. cand.text .. "'")
            yield(Candidate("null_add", cand.start, cand._end, auto, "  💡"))
        end
    end
end

return if_null_add_filter
