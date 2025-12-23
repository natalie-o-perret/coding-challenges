const std = @import("std");

fn isNice(s: []const u8) bool {
    // Check for a pair that appears at least twice without overlapping
    var has_pair = false;
    var i: usize = 0;
    while (i < s.len - 1) : (i += 1) {
        const pair = s[i .. i + 2];
        // Look for the same pair starting at least 2 positions later
        if (std.mem.indexOf(u8, s[i + 2 ..], pair) != null) {
            has_pair = true;
            break;
        }
    }
    if (!has_pair) {
        return false;
    }

    // Check for a letter that repeats with exactly one letter between
    var j: usize = 0;
    while (j < s.len - 2) : (j += 1) {
        if (s[j] == s[j + 2]) {
            return true;
        }
    }

    return false;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    // Test cases with assertions
    std.debug.assert(isNice("qjhvhtzxzqqjkmpb") == true);
    std.debug.assert(isNice("xxyxx") == true);
    std.debug.assert(isNice("uurcxstgmygtbstg") == false);
    std.debug.assert(isNice("ieodomkazucvgmuy") == false);

    const input = try std.fs.cwd().readFileAlloc(allocator, "../input.txt", 1024 * 1024);
    defer allocator.free(input);

    var count: u32 = 0;
    var lines = std.mem.splitSequence(u8, std.mem.trim(u8, input, &std.ascii.whitespace), "\n");
    while (lines.next()) |line| {
        if (isNice(line)) {
            count += 1;
        }
    }

    std.debug.print("Zig: {d}\n", .{count});
}
