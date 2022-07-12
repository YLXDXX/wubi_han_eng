local is_split_sentence
local wordninja_split

local function capture(cmd)
   local f = assert(io.popen(cmd, 'r'))
   local s = assert(f:read('*a'))
   f:close()
   return s
end

local function init(env)
   is_split_sentence = env.engine.schema.config:get_bool('wubi98_dz/split_en')
   if not is_split_sentence then
      wordninja_split = function(sentence)
         return sentence
      end
      return
   end
   if true then
      wordninja_split = function(sentence)
         return capture("~/.local/share/fcitx5/rime/lua/fengci/wordninja" .. " -n '" .. sentence .. "'")
      end
      return
   end
end






local function enhance_filter(input, seg)
    if (is_split_sentence) then
        if (utf8.len(input) >= 5) then
            sentence = wordninja_split(input)
            yield(Candidate("sentence", seg.start, seg._end, sentence, " 💡"))
        end
    else
        --- yield(Candidate("word", seg.start, seg._end, input .. " ", cand.comment))
    end
end



---local function wordninja_splittt (sentence)
---    return capture("~/.local/share/fcitx5/rime/lua/fengci/wordninja" .. " -n '" .. sentence .. "'")
---end
--local function enhance_filter(input, seg)
--   sentence = wordninja_split(input)
--   yield(Candidate("sentence", seg.start, seg._end, sentence, " 💡"))
--end

return { enhance_filter = { init = init, func = enhance_filter} }




