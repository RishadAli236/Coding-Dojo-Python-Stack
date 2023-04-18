from modules import ninja, cat

ninja_cat = cat.Cat("neko", "cat", ["taijutsu", "genjutsu"],"korat", "meow")
shinobi = ninja.Ninja("Rishad", "Yasin", ["ninja pill"], ["ninja pill"], ninja_cat )
shinobi.feed().walk().bathe()
print(f"Pet Energy: {ninja_cat.energy}", f"Pet Health: {ninja_cat.health}")
