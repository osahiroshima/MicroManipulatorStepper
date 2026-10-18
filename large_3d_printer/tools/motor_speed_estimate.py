"""ステッピングモーターの「トルクが落ち始める速度」の概算。

モデル（簡易）:
  電源電圧 V で、目標電流 I を流しきれる最大の回転速度を求める。
  コイル両端に必要な電圧 ≒ sqrt( (I*R + Ke*w)^2 + (we*L*I)^2 )
    R  : 巻線抵抗 [Ω]
    L  : インダクタンス [H]
    Ke : 逆起電力定数 [V/(rad/s)]  ≒ 保持トルク / 定格電流 で近似
    w  : 機械角速度 [rad/s]
    we : 電気角速度 = 極対数 * w
  この値が V を超える速度から、流せる電流＝トルクが下がり始める。
あくまで目安で、実機は共振やドライバーの特性でこれより低くなることが多い。
"""
import math

# ST-42BYH1004-5013 データシートより
R = 5.0            # Ω/相
L = 11.5e-3        # H/相
I_RATED = 1.0      # A/相
T_HOLD = 0.43      # N·m（4.4 kgf·cm）
POLE_PAIRS = 100   # 0.9° モーター（1回転 400 フルステップ）

KE = T_HOLD / I_RATED
MM_PER_REV = 40.0  # GT2 ベルト + 20 歯プーリー


def corner_speed(v_supply, i_run):
    """電流 i_run を流しきれる最大回転数 [rev/s] を二分法で求める。"""
    def needed(w):
        we = POLE_PAIRS * w
        return math.hypot(i_run * R + KE * w, we * L * i_run)
    lo, hi = 0.0, 200.0
    if needed(lo) > v_supply:
        return 0.0
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if needed(mid) <= v_supply else (lo, mid)
    return lo / (2 * math.pi)


if __name__ == "__main__":
    print(f"{'電源':>5} {'電流':>6} {'回転数':>8} {'ベルト速度':>10}")
    for v in (5, 12, 24, 36, 48):
        for i in (0.6, 0.8, 1.0):
            rps = corner_speed(v, i)
            print(f"{v:>4}V {i:>5.1f}A {rps:>6.2f}rps {rps * MM_PER_REV:>8.0f}mm/s")
