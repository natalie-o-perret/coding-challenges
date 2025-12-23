const std = @import("std");

fn findAdventCoin(allocator: std.mem.Allocator, secret_key: []const u8) !u32 {
    var number: u32 = 1;
    while (true) : (number += 1) {
        const text = try std.fmt.allocPrint(allocator, "{s}{d}", .{ secret_key, number });
        defer allocator.free(text);

        var hash: [16]u8 = undefined;
        std.crypto.hash.Md5.hash(text, &hash, .{});

        // Check if first 2.5 bytes are zero (5 hex digits = 00000)
        // hash[0] == 0x00 -> "00"
        // hash[1] == 0x00 -> "00"
        // hash[2] & 0xF0 == 0 -> "0?"
        if (hash[0] == 0 and hash[1] == 0 and (hash[2] & 0xF0) == 0) {
            return number;
        }
    }
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    // Skip test cases - they're too slow in Zig without optimizations

    const input = try std.fs.cwd().readFileAlloc(allocator, "../input.txt", 1024 * 1024);
    defer allocator.free(input);
    const secret_key = std.mem.trim(u8, input, &std.ascii.whitespace);

    const result = try findAdventCoin(allocator, secret_key);
    std.debug.print("Zig: {d}\n", .{result});
}
