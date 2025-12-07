# กราฟตัวอย่าง (ระยะทางระหว่างจังหวัด)
graph = {
    "กรุงเทพ": {"อยุธยา": 80, "นครปฐม": 60},
    "อยุธยา": {"กรุงเทพ": 80, "ลพบุรี": 70},
    "ลพบุรี": {"อยุธยา": 70, "นครสวรรค์": 140},
    "นครปฐม": {"กรุงเทพ": 60, "สุพรรณบุรี": 50},
    "สุพรรณบุรี": {"นครปฐม": 50, "ชัยนาท": 90},
    "นครสวรรค์": {"ลพบุรี": 140, "ชัยนาท": 60},
    "ชัยนาท": {"สุพรรณบุรี": 90, "นครสวรรค์": 60}
}
 
 
def dijkstra(graph, start, end):
    # กำหนดระยะทางเริ่มต้นเป็น inf ยกเว้น start = 0
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
 
    visited = set()
    previous = {node: None for node in graph}
 
    while len(visited) < len(graph):
        # เลือก node ที่ยังไม่ถูกเยี่ยมและมี dist น้อยสุด
        current = None
        current_dist = float('inf')
 
        for node in graph:
            if node not in visited and dist[node] < current_dist:
                current = node
                current_dist = dist[node]
 
        if current is None:
            break
 
        visited.add(current)
 
        # อัปเดตระยะทาง
        for neighbor, weight in graph[current].items():
            new_dist = dist[current] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                previous[neighbor] = current
 
    # สร้างเส้นทางย้อนหลัง
    path = []
    node = end
    while node:
        path.append(node)
        node = previous[node]
 
    path.reverse()
    return dist[end], path
 
 
# ===== MAIN PROGRAM =====
start = input("เลือกจังหวัดเริ่มต้น: ")
end = input("เลือกจังหวัดปลายทาง: ")
 
if start not in graph or end not in graph:
    print("จังหวัดไม่อยู่ในระบบ")
else:
    distance, path = dijkstra(graph, start, end)
    print("\n=== ผลลัพธ์การคำนวณ ===")
    print("ระยะทางที่สั้นที่สุด:", distance, "กม.")
    print("เส้นทาง:", " → ".join(path))
