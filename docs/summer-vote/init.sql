-- 夏日消暑神器·人气饮品大调查
-- 在 Supabase SQL Editor 中执行

CREATE TABLE summer_votes (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  beverage_name TEXT NOT NULL,
  session_id UUID NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_summer_votes_beverage ON summer_votes(beverage_name);

ALTER TABLE summer_votes ENABLE ROW LEVEL SECURITY;

CREATE POLICY "allow_public_insert" ON summer_votes
  FOR INSERT TO anon WITH CHECK (true);

CREATE POLICY "allow_public_select" ON summer_votes
  FOR SELECT TO anon USING (true);
